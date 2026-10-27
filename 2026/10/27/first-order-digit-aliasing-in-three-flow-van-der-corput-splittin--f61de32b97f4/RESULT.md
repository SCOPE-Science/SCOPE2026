# First-order digit aliasing in three-flow van der Corput splitting

## Finding

A perfectly low-discrepancy, one-dimensional driver need not produce balanced quasi-random permutations for three-flow splitting. With the binary radical-inverse sequence and the standard descending Fisher–Yates shuffle, only **two of six** orders occur, and they have limiting frequencies \(1/3\) and \(2/3\). The imbalance leaves a nonzero commutator term and, for an explicit three-flow linear system, a sharp **first-order** global error.

For fixed \(T>0\), set \(h=T/N\). For arbitrary fixed real or complex square matrices \(A_1,A_2,A_3\), write
\[
B=A_1+A_2+A_3,\qquad K=[A_2,A_1]+[A_2,A_3]+[A_1,A_3],\qquad [X,Y]=XY-YX.
\]
Let \(U_N\) be the product of the \(N\) splitting steps specified below, with latest step acting on the left. The full operator asymptotic is
\[
\boxed{\;U_N-e^{TB}=-\frac h6\int_0^T e^{(T-s)B}K e^{sB}\,ds+O_{T,A}(h^2(1+\log N)).\;}
\]
The residual is in any fixed matrix operator norm. The integral need not vanish. In particular, for \(A_1=E_{12}\), \(A_2=E_{23}\), and \(A_3=I_3\), where \(E_{ij}\) denotes the standard matrix unit,
\[
\boxed{\;\lim_{N\to\infty}\frac{\|U_N-e^{TB}\|_2}{h}=\frac{T e^T}{6}>0.\;}
\]
The obstruction is not a generic claim about all quasi-random shuffles. It is a fully specified, natural implementation of a three-flow, serial-radical-inverse shuffle.

## Assumptions and scope

For integers \(m\ge0\), write \(m=\sum_{j\ge0}b_j2^j\) with binary digits \(b_j\in\{0,1\}\), and set \(\varphi_2(m)=\sum_{j\ge0}b_j2^{-j-1}\). Define \(q_m=\varphi_2(m)\) for \(m\ge1\). For time steps numbered \(n=0,\dots,N-1\), independently initialize \(\pi=(1,2,3)\). In **descending** Fisher–Yates order, swap positions \(3\) and \(j_3=1+\lfloor3q_{2n+1}\rfloor\), then swap positions \(2\) and \(j_2=1+\lfloor2q_{2n+2}\rfloor\), counting array positions from one. The resulting \(\pi=(\pi_1,\pi_2,\pi_3)\) defines the step
\[
M_n(h)=e^{hA_{\pi_3}}e^{hA_{\pi_2}}e^{hA_{\pi_1}},\qquad U_N=M_{N-1}(h)\cdots M_0(h).
\]
The reference solution is \(e^{TB}\). All matrices are fixed and finite-dimensional; constants may depend on their norms and \(T\), but not on \(N\). The same proof works for bounded operators on a Banach space.

## Proof

**1. Exact digit correlation and permutation law.** Binary radical inversion gives
\[
q_{2n+1}=\frac{1+\varphi_2(n)}2,\qquad q_{2n+2}=\frac{\varphi_2(n+1)}2<\frac12.
\]
Consequently \(j_2=1\) on every step. Also \(j_3=2\) precisely when \(\varphi_2(n)<1/3\), and \(j_3=3\) otherwise. Applying the two swaps shows
\[
\pi_n=\begin{cases}(3,1,2),&\varphi_2(n)<1/3,\\(2,1,3),&\varphi_2(n)\ge1/3.\end{cases}
\]
Every dyadic interval \([a2^{-m},(a+1)2^{-m})\) selects one residue class of indices modulo \(2^m\), hence among the first \(N\) radical-inverse values its counting discrepancy is at most one. The interval \([0,1/3)\) is a disjoint union of consecutive dyadic intervals of lengths \(2^{-2},2^{-4},2^{-6},\dots\) (the binary expansion of \(1/3\) is \(0.010101\ldots\)). Retain \(J=\lceil\log_4(N+1)\rceil\) such intervals. Their total count error is at most \(J\); the remaining interval lies in one dyadic interval of length \(4^{-J}\), which contains at most \(N4^{-J}+1\le2\) sample indices. Its expected count is less than one. Thus, uniformly for all \(N\ge1\),
\[
\#\{0\le n<N:\varphi_2(n)<1/3\}=N/3+O(1+\log N).
\]
This bound holds for every prefix, as required below.

**2. Local commutator coefficients.** Set \(E_h=e^{hB}\). Taylor expansion of the three exponentials, uniformly for small \(h\), gives
\[
M_n(h)-E_h=h^2 C_n+O_A(h^3),\quad C_n=\begin{cases}K/2,&\pi_n=(3,1,2),\\-K/2,&\pi_n=(2,1,3).\end{cases}
\]
In particular \(\bar C=(1/3)(K/2)+(2/3)(-K/2)=-K/6\). Part 1 implies \(\sup_{m\le N}\|\sum_{n<m}(C_n-\bar C)\|=O_A(1+\log N)\).

**3. Propagation and Abel summation.** The exact telescoping identity is
\[
U_N-E_h^N=\sum_{n=0}^{N-1}M_{N-1}\cdots M_{n+1}(M_n-E_h)E_h^n.
\]
Submultiplicative bounds on the fixed generators give \(\|M_n\|,\|E_h\|\le e^{hL}\) for suitable \(L\). The difference between any product of \(O(N)\) split factors and the corresponding exact factors is \(O_{T,A}(h)\), because each one-step defect is \(O_A(h^2)\). Replacing left propagators by exact exponentials and inserting the local expansion therefore changes the full sum only by \(O_{T,A}(h^2)\):
\[
U_N-e^{TB}=h^2\sum_{n=0}^{N-1}e^{(N-1-n)hB}C_n e^{nhB}+O_{T,A}(h^2).
\]
For \(W_n=e^{(N-1-n)hB}\,K\,e^{nhB}\), the bound \(\|W_n\|=O_{T,A}(1)\) and the adjacent variation \(\|W_{n+1}-W_n\|=O_{T,A}(h)\) follow from the differentiability of matrix exponentials. Discrete summation by parts with the prefix discrepancy from part 2 yields
\[
h^2\sum_{n=0}^{N-1}e^{(N-1-n)hB}(C_n-\bar C)e^{nhB}=O_{T,A}(h^2(1+\log N)).
\]
The remaining constant-coefficient sum is a Riemann sum:
\[
h^2\sum_{n=0}^{N-1}e^{(N-1-n)hB}\bar C e^{nhB}
=h\int_0^T e^{(T-s)B}\bar C e^{sB}\,ds+O_{T,A}(h^2).
\]
Substituting \(\bar C=-K/6\) proves the general asymptotic.

**4. Exact matrix witness.** Take \(A_1=E_{12}\), \(A_2=E_{23}\), and \(A_3=I_3\), and write \(S=E_{12}+E_{23}\). Then \(S^2=E_{13}\) and \(S^3=0\). The two possible step matrices are exactly
\[
M_{(3,1,2)}(h)=e^h(I_3+hS),\qquad M_{(2,1,3)}(h)=e^h(I_3+hS+h^2 E_{13}).
\]
Let \(c_N\) count steps of the latter type. Multiplying these upper-triangular matrices, using \(SE_{13}=E_{13}S=0\), gives
\[
U_N=e^T\bigl(I_3+TS+h^2(\tbinom N2+c_N)E_{13}\bigr),\quad e^{TB}=e^T\bigl(I_3+TS+\tfrac12 T^2E_{13}\bigr).
\]
Thus the identity, **exact for every positive integer \(N\)**, is
\[
U_N-e^{TB}=e^Th^2(c_N-N/2)E_{13}.
\]
Since \(c_N=2N/3+O(1+\log N)\), the asserted positive limit follows from \(\|E_{13}\|_2=1\). Moreover \(K=-E_{13}\) in this example, so the general integral formula gives the same constant. Taking a sufficiently small nonzero perturbation \(A_3=I_3+\delta E_{31}\) retains a nonzero leading integral by continuity and makes all three pairwise commutators nonzero.

## Verification

The standalone `check.py` uses exact rational arithmetic for radical-inverse values and nilpotent matrix products. It checks that only the stated two orderings occur, confirms the exact \(3\times3\) product identity for all \(1\le N\le128\), and prints normalized errors along increasing dyadic prefixes. These finite tests verify the reproducibility of symbolic identities for tested inputs, **not** the universal assertions. The proof above supplies the infinite quantifiers, the logarithmic counting bound, and the asymptotic limit. To run: `python3 check.py` (standard Python library only).

## Relationship to prior work

Li, Liu, and Wan (2026), arXiv:2603.27654v1, define operator splitting with serial quasi-random entries fed into a Fisher–Yates shuffle; they prove an essentially second-order result for **two** subflows and include a three-subflow numerical test. Their Section 6 identifies extending rigorous analysis to general \(p\) as future work. The present result distinguishes a particular **three**-flow binary/descending-shuffle implementation: single-coordinate low discrepancy does not imply balanced distributions of consecutive shuffle decisions. Its nonzero leading global commutator term is not a special case of their two-flow theorem. Classic symmetric Strang products and uniformly randomized product formulas use different symmetry or randomization mechanisms. The distinction is in the joint digit structure, not merely in the terminology of randomized splitting.

## Limitations

The exact choice of descending in-place Fisher–Yates updates, assignment of consecutive radical-inverse entries, initial index, and binary base are essential. An ascending Fisher–Yates convention, a scrambled or higher-dimensional low-discrepancy driver, shifted indexing, or other ordering map may behave differently. The motivating manuscript names Fisher–Yates abstractly rather than fixing all such implementation conventions in mathematical notation, so the theorem does **not** claim the authors' experimental software uses this exact variant or that their numerical findings are false. A nonzero leading term is generic but can vanish under commutator cancellation. This theorem is for fixed bounded matrices (and bounded Banach-space generators), not a convergence characterization of nonlinear PDE splitting or unbounded operators.

## References

1. L. Li, Y. Liu, C. Wan, *Quasi-random splitting method for accurate and efficient multiphysics simulation*, arXiv:2603.27654v1, March 29, 2026, https://arxiv.org/html/2603.27654v1 . Sections 2–4, 5.2.2, 6 inspected.
2. C. Cho, D. W. Berry, M. Hsieh, *Doubling the Order of Approximation via the Randomized Product Formula*, Physical Review A 109, 062431 (2024). Context for randomized orders; different from a single deterministic binary sequence.
3. R. I. McLachlan and G. R. W. Quispel, *Splitting methods*, Acta Numerica 11 (2002), 341–434. General product-formula background, not a claim about this digit-specific shuffle.
