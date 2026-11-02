# A sharp logarithmic error subsequence for three-flow quasi-random splitting

## Finding

Consider the base-two van der Corput ordering used with the direct lexicographic point-to-permutation decoder for three subflows. An explicit bounded, noncommuting, three-generator matrix problem attains an error of order \(h^2\log(1/h)\), showing that the logarithmic factor in the corresponding upper convergence estimate cannot in general be dropped.

Specifically, let \(E_{ij}\) denote the \(4\times4\) real matrix unit and fix \(T>0\). Set \(A_1=E_{12}\), \(A_2=E_{23}\), \(A_3=E_{34}\), and \(J=A_1+A_2+A_3\). Let \(\varphi_2(n)\) be the binary radical inverse, \(\pi_n\) the lexicographic permutation of \((1,2,3)\) with zero-based rank \(\lfloor6\varphi_2(n)\rfloor\), and
\[
M_n(h)=e^{hA_{\pi_n(3)}}e^{hA_{\pi_n(2)}}e^{hA_{\pi_n(1)}},\qquad
U_N(T)=M_N(T/N)\cdots M_1(T/N).
\]
For every integer \(k\ge1\), define \(N_k=(5\cdot4^k-2)/6\) and \(h_k=T/N_k\). Then the following is **an exact equality**, not just an asymptotic estimate:
\[
\boxed{\bigl(U_{N_k}(T)-e^{TJ}\bigr)_{13}=-\frac{2k-1}{2}\,h_k^2.}
\]
Hence
\[
\boxed{\lim_{k\to\infty}\frac{\bigl(U_{N_k}(T)-e^{TJ}\bigr)_{13}}{h_k^2\log N_k}=-\frac1{\log4}.}
\]
In particular, for any subordinate matrix norm, the global error is not uniformly \(O(h^2)\) along this sequence. The logarithmic scale is attained with exactly three nonzero, genuinely noncommuting subflows.

## Assumptions and scope

The matrices act on \(\mathbb R^4\) with ordinary exact exponentials and exact arithmetic. All steps have equal size \(h=T/N\), the total time is fixed and positive, and each of the three subflows occurs exactly once per step in the direct-decoder chronological order. The first sample is \(\varphi_2(1)=1/2\), not \(\varphi_2(0)=0\). The ordered product places later steps to the left. The decoder is the **single-point direct lexicographic decoder**, distinct from an earlier multi-point shuffle implementation of quasi-random splitting. There is no assertion about arbitrary quasi-random sequences, other decoders, nonlinear flows, or stochastic perturbations.

## Proof

**1. Reduce the matrix error to an exact signed count.** For the selected matrix units, \(A_i^2=0\) and \(e^{hA_i}=I+hA_i\). The only ordered pair of split generators whose product contributes to matrix entry \((1,3)\) is \(A_1A_2=E_{13}\). Two different time steps always contribute \(h^2\) to that entry when the earlier step supplies \(A_2\) and the later supplies \(A_1\), accounting for \(\binom N2\) pairs. A single step contributes an additional \(h^2\) precisely when its chronological ordering places operator \(2\) before operator \(1\). Thus, if \(\xi_n=+1\) for that latter ordering and \(\xi_n=-1\) otherwise, and \(D(N)=\sum_{n=1}^N\xi_n\), then
\[
\bigl(U_N(T)\bigr)_{13}=h^2\left[\binom N2+\frac{N+D(N)}2\right]
=\frac{T^2}{2}+\frac{h^2D(N)}2.
\]
Since \(J^2=E_{13}+E_{24}\), \(J^4=0\), and \((e^{TJ})_{13}=T^2/2\), the exact error is \(h^2D(N)/2\). No approximation or ignored higher-order remainder is involved.

**2. Identify the decoder's sign function.** The six lexicographic permutations are \(123,132,213,231,312,321\); their signs are respectively \(-1,-1,+1,+1,-1,+1\). Equivalently, for dyadic \(x\in[0,1)\), define
\[
f(x)=\begin{cases}-1,&0\le x<1/3,\\+1,&1/3\le x<2/3,\\-1,&2/3\le x<5/6,\\+1,&5/6\le x<1,\end{cases}
\qquad \xi_n=f(\varphi_2(n)).
\]
All radical-inverse values are dyadic, hence no value falls on the three non-dyadic breakpoints. Define also \(g(x)=-1\) on \([0,1/3)\cup[5/6,1)\), and \(g(x)=+1\) on \([1/3,5/6)\).

**3. Establish a four-digit block identity.** Binary digit reversal gives
\[
\varphi_2(4j+r)=\frac{\varphi_2(j)}4+\frac{\operatorname{rev}_2(r)}4,
\qquad r\in\{0,1,2,3\},
\]
where \(\operatorname{rev}_2(0),\operatorname{rev}_2(1),\operatorname{rev}_2(2),\operatorname{rev}_2(3)\) are respectively \(0,2,1,3\). Direct insertion into the four pieces of \(f\) yields, at every dyadic \(x=\varphi_2(j)\),
\[
\sum_{r=0}^{3}f\!\left(\frac{x+\operatorname{rev}_2(r)}4\right)=f(x)+g(x).
\]
Likewise, the two half-interval evaluations satisfy \(g(x/2)+g((1+x)/2)=0\) for every dyadic \(x\in[0,1)\). This latter identity implies
\[
\sum_{j=0}^{m-1}g(\varphi_2(j))=g(\varphi_2(m-1))
\quad\text{when }m\text{ is odd},
\]
because all preceding indices occur in complete even-odd pairs.

**4. Derive the exact recursion at odd prefixes.** Extend \(D\) by \(D(0)=0\), and recall \(f(\varphi_2(0))=-1\). Summing the four-digit identity over \(j=0,\ldots,m-1\) and handling indices \(4m\) and \(4m+1\) separately gives
\[
D(4m+1)-D(m)=-f(\varphi_2(m))+
\sum_{j=0}^{m-1}g(\varphi_2(j))+
 f(\varphi_2(4m))+f(\varphi_2(4m+1)).
\]
When \(m=2r+1\) is odd, write \(x=\varphi_2(r)\). Then
\[
\varphi_2(m)=\frac{1+x}{2},\quad
\varphi_2(m-1)=\frac{x}{2},\quad
\varphi_2(4m)=\frac{1+x}{8},\quad
\varphi_2(4m+1)=\frac{5+x}{8}.
\]
For the three ranges \(x\in[0,1/3)\), \(x\in[1/3,2/3)\), and \(x\in[2/3,1)\), the respective four summands in the last display for \(D(4m+1)-D(m)\), listed in order, are
\[
(-1,-1,-1,+1),\quad(+1,-1,-1,-1),\quad(-1,+1,-1,-1).
\]
Each tuple sums to \(-2\). Thus the **exact odd-prefix recursion** holds:
\[
\boxed{D(4m+1)=D(m)-2\qquad(m\ge1\text{ odd}).}
\]
Now \(D(3)=-1\), \(N_1=3\), and \(N_{k+1}=4N_k+1\); all \(N_k\) are odd. Induction yields \(D(N_k)=1-2k\). Substituting into step 1 proves the exact entry identity. Finally, \(\log N_k=k\log4+O(1)\) proves the stated limit.

## Verification

The supplied Python 3 script `verify.py` uses only the standard library. It checks 10,000 four-digit block identities, 10,000 paired-cancellation identities, 750 odd-prefix recursions, nine exact subsequence counts, five **actual** four-by-four rational matrix products at \(N=3,13,53,213,853\), and an additional rational matrix product at \(T=7/5\). The executed script reported **20,765 exact-rational passing assertions**. These finite checks are consistency evidence; the preceding algebra is the proof for all \(k\).

## Relationship to prior work

Li, Liu, and Wan, *Quasi-random splitting method for accurate and efficient multiphysics simulation* (arXiv:2603.27654, first submitted 29 March 2026; direct-decoder revision v2 dated 19 October 2026), establish a general bounded-linear error **upper bound** of order \(O(h^2(1+\log N))\). This finding proves that this logarithmic factor is necessary for the specific binary radical-inverse direct decoder, by an exact three-operator instance. It does not assert a new general discrepancy inequality.

Classical work on van der Corput discrepancy, including explicit arithmetic formulas attributed to Faure and the analysis by Beretti, explains why logarithmic discrepancy is natural for non-dyadic intervals. Those discrepancy facts do not themselves state the present exact numerical **operator-splitting error**, the matrix-unit witness, or the subsequence coefficient. The arithmetic discrepancy recursion here is proved directly rather than claimed as a new general discrepancy theorem.

## Limitations

The result is a worst-case lower bound for one precisely fixed sampler/decoder, not a typical-case estimate. The exact subsequence does not characterize all times or all matrix entries. The chosen operators are bounded, upper-triangular, and nilpotent, and the demonstration uses an exact full subflow product. It rules out a universal \(O(h^2)\) guarantee for the designated decoder; it does not rule out second order for other quasi-random point sets, alternative decoders, additional symmetrization, or restricted operator classes. No external independent audit has yet been performed.

## References

1. L. Li, Y. Liu, and C. Wan, *Quasi-random splitting method for accurate and efficient multiphysics simulation*, arXiv:2603.27654, versions 1 (29 March 2026) and 2 (19 October 2026). https://arxiv.org/abs/2603.27654 ; https://arxiv.org/pdf/2603.27654
2. T. Beretti, *On the distribution of the van der Corput sequences*, Archiv der Mathematik 120 (2023), 283–295, https://doi.org/10.1007/s00013-022-01811-4.
