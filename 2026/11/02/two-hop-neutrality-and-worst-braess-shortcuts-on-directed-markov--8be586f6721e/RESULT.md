# Two-hop neutrality and worst Braess shortcuts on directed Markov rings

## Finding

For a continuously evolving directed Markov ring, inserting a forward shortcut can make integrated relaxation **worse**, despite increasing the available rate of motion. A jump advancing exactly two vertices is **neutral** for every added rate when the original ring rates are equal; every genuine longer jump makes integrated relaxation strictly worse. More generally, an explicit reciprocal-rate expression determines whether each added link helps or hurts on an *arbitrary heterogeneous directed ring*.

**Theorem (all rates and all shortcut lengths).** Fix an integer \(n\ge3\) and positive rates \(r_0,\ldots,r_{n-1}\). The unperturbed continuous-time chain jumps from vertex \(i\) to \(i+1\pmod n\) at rate \(r_i\). Add rate \(t\ge0\) from vertex \(0\) to vertex \(k\), with \(1\le k\le n-1\). Let \(L(t)=-Q(t)\) be the row Laplacian and put
\[
H(t)=\int_0^\infty\left(\operatorname{tr}(e^{-sL(t)})-1\right)\,ds
=\operatorname{tr}(L(t)^\#).
\]
This is the continuous-time Kemeny relaxation functional; the integral converges and is real, even when the nonzero eigenvalues are complex. Define \(w_i=r_i^{-1}\), \(S=\sum_{i=0}^{n-1}w_i\), \(E_2=\sum_{0\le i<j<n}w_iw_j\),
\[
A=\sum_{i=1}^{k-1}w_i,\quad
B=\sum_{i=k}^{n-1}w_i,\quad
C=\sum_{k\le i<j<n}w_iw_j+AB.
\]
Empty sums vanish. Then the **exact law** for all \(t\ge0\) is
\[
\boxed{H(t)=\frac{E_2+(t/r_0)C}{S+(t/r_0)B}}.
\]
In particular, the sign of the link's effect is independent of its added rate:
\[
\boxed{\operatorname{sgn}(H'(t))=\operatorname{sgn}(CS-BE_2)}.
\]
Thus this one-link perturbation is strictly beneficial, exactly neutral, or strictly harmful at **every** positive rate, according as \(CS-BE_2\) is negative, zero, or positive.

For **unit rates**, the law simplifies to
\[
\boxed{H_{n,k}(t)=\frac{n(n-1)+t(n-k)(n+k-3)}{2[n+t(n-k)]}},
\]
and
\[
\boxed{H_{n,k}(t)-H_{n,k}(0)=\frac{t(n-k)(k-2)}{2[n+t(n-k)]}}.
\]
Consequently, for all \(t>0\): increasing the existing one-step rate (\(k=1\)) helps; the two-step shortcut (\(k=2\)) leaves \(H\) unchanged; and each shortcut of length \(k\ge3\) increases \(H\). This paradox is first possible at \(n=4\). The neutrality of the two-hop edge is specific to equal baseline rates: on the four-state ring, for \(k=2\) and \(t=1\), rates \((1,2,1,1)\) decrease the functional from \(9/7\) to \(13/11\), whereas rates \((1,1/2,1,1)\) increase it from \(9/5\) to \(2\).

**Worst single shortcut.** For fixed \(n\ge4\) and \(t>0\), among the genuine shortcuts \(2\le k\le n-1\), the largest increase is obtained by choosing an integer \(y=n-k\) maximizing
\[
 g_t(y)=\frac{y(n-2-y)}{n+ty},\qquad 1\le y\le n-3.
\]
The maximizing integers are the one or two nearest feasible integers to the unique real critical point
\[
\boxed{y_c=\frac{\sqrt{n^2+tn(n-2)}-n}{t}},
\]
with their exact comparison settled by
\[
\operatorname{sgn}(g_t(y+1)-g_t(y))
=\operatorname{sgn}\left(n(n-2y-3)-ty(y+1)\right).
\]
In particular the worst value of \(y\) is nonincreasing as \(t\) grows (the worst shortcut moves forward toward \(k=n-1\)); a tie between \(y\) and \(y+1\) occurs exactly at
\[
t=\frac{n(n-2y-3)}{y(y+1)}>0
\]
when that parameter is positive and both indices are feasible. For \(n=6\), the worst shortcut is \(k=4\) for \(0<t<3\), both \(k=4,5\) tie for \(t=3\), and \(k=5\) wins for \(t>3\).

## Assumptions and scope

All rings are directed one-way and finite. The jump rates \(r_i\) are strictly positive; the added rate \(t\) is nonnegative. The generator \(Q\) acts on row distributions; \(Q_{i,i+1}=r_i\), \(Q_{ii}=-r_i\), with the corresponding row-\(0\) changes \(Q_{0k}\mathrel{+}=t\) and \(Q_{00}\mathrel{-}=t\). For \(k=1\), the new arc is parallel to the existing forward arc; for \(k\ge2\) it is a distinct shortcut. All cyclic indices are reduced modulo \(n\). The original ring ensures irreducibility for every \(t\ge0\), so zero is a simple eigenvalue of \(L(t)\), and every other eigenvalue has strictly positive real part. The rate dependent statement covers every \(n\ge3\); the worst-shortcut classification concerns \(n\ge4\).

## Proof

**Step 1 (exact characteristic polynomial).** Put \(P=\prod_{i=0}^{n-1}r_i\) and \(M(z)=zI+L(0)\). The diagonal entries of \(M\) are \(z+r_i\), and its only nonzero off-diagonal entries are \(-r_i\) in cyclic successor positions. Only the identity and full-cycle permutations contribute to its determinant, so
\[
\det M(z)=\prod_{i=0}^{n-1}(z+r_i)-P.
\]
As \(L(t)=L(0)+te_0(e_0-e_k)^\top\), the rank-one determinant identity gives
\[
\det(zI+L(t))=\det M(z)+t(e_0-e_k)^\top\operatorname{adj}(M(z))e_0.
\]
Deleting row and column \(0\) gives
\[
[\operatorname{adj}M(z)]_{00}=\prod_{i=1}^{n-1}(z+r_i).
\]
Expanding the cofactor for the unique directed chain from \(k\) to \(0\) gives
\[
[\operatorname{adj}M(z)]_{k0}=\left(\prod_{i=k}^{n-1}r_i\right)
\prod_{i=1}^{k-1}(z+r_i).
\]
Therefore
\[
\boxed{\det(zI+L(t))=\prod_{i=0}^{n-1}(z+r_i)-P+
 t\left[\prod_{i=1}^{n-1}(z+r_i)-
 \left(\prod_{i=k}^{n-1}r_i\right)\prod_{i=1}^{k-1}(z+r_i)\right]}.
\]
The constant term vanishes, as it must because \(L(t)\mathbf 1=0\).

**Step 2 (the relaxation trace is a coefficient ratio).** Let \(\lambda_1,\ldots,\lambda_{n-1}\) be the nonzero eigenvalues of \(L(t)\), counted with algebraic multiplicity. Irreducibility implies \(\operatorname{Re}\lambda_j>0\), and Jordan's formula for the matrix exponential yields \(H(t)=\sum_j\lambda_j^{-1}\). Writing
\[
\det(zI+L(t))=a_1(t)z+a_2(t)z^2+\cdots+z^n
\]
gives \(a_1(t)=\prod_j\lambda_j>0\) and \(a_2(t)/a_1(t)=\sum_j\lambda_j^{-1}\). Expand the exact determinant through quadratic order, using the elementary reciprocal-rate symmetric sums. Its coefficients are
\[
a_1(t)=P\left[S+\frac{t}{r_0}B\right],\qquad
a_2(t)=P\left[E_2+\frac{t}{r_0}\bigl(E_2(B)+AB\bigr)\right].
\]
Taking the ratio proves the claimed heterogeneous-rate law. Its derivative is
\[
H'(t)=\frac{CS-BE_2}{r_0\left[S+(t/r_0)B\right]^2},
\]
so the sign is independent of \(t\).

**Step 3 (equal-rate sharp classification).** Under \(r_i=1\), one has \(S=n\), \(E_2=n(n-1)/2\), \(B=n-k\), \(A=k-1\), and
\[
C=\frac{(n-k)(n+k-3)}2.
\]
Substituting gives the displayed rational expression and, after subtracting \((n-1)/2\), the exact factor \(k-2\). This establishes every asserted sign, including equality for all \(t\) at \(k=2\).

**Step 4 (worst shortcut and thresholds).** For fixed \(n,t\), the positive change at \(k\ge3\), apart from the common factor \(t/2\), equals \(g_t(y)\), where \(y=n-k\). Differentiation gives
\[
 g_t'(y)=\frac{n(n-2)-2ny-ty^2}{(n+ty)^2}.
\]
Its numerator is strictly decreasing for \(y\ge0\), with exactly one positive zero, namely \(y_c\). Hence \(g_t\) increases and then decreases. Exact cross-multiplication yields the displayed adjacent-difference sign and tie thresholds. These signs become smaller as \(t\) grows, so no larger maximizer \(y\) can newly overtake a smaller one: the maximizers move nonincreasingly as claimed. At \(n=6\), the only positive comparison threshold is \(t=3\), giving the stated three regimes. This proves the theorem.

## Verification

The standalone Python 3 standard-library script `verify.py` forms the generator directly, computes the characteristic polynomial by an exact-rational Faddeev–LeVerrier recurrence independently of the proposed cofactor formula, and compares both coefficients for multiple nonuniform rates, chord locations, and added rates. It separately checks the equal-rate functional, every sign class, adjacent comparison formula, and two heterogeneous examples. Running `python verify.py` produced `PASS 9920 exact rational assertions`. These finite computations are reproducibility checks, **not** substitutes for the all-parameter proof above.

## Relationship to prior work

Catral, Kirkland, Neumann and Sze (2010) prove general Kemeny representations, low-rank perturbation statements and a graph-class invariance theorem. Their Section 6 requires equal lengths for every directed cycle to obtain invariance across all transition probabilities; a one-chord ring generally has two different cycle lengths, so it does **not** give the two-hop neutral continuous-time law or the worst-shortcut cascade. Kirkland (2010) optimizes the discrete-time expected mixing measure over all transition matrices of a given directed graph, a different feasible family and objective from the fixed-positive-base-rate, continuous-time added-chord function here. Hunter (2012) develops Markov-chain perturbation identities, and Kirkland and Zeng (2016) analyze Braess-type increases for undirected tree random walks. The present claim is an explicit all-rate directed-cycle classification, not an assertion that general Kemeny or perturbation techniques are new.

## Limitations

The theorem concerns the integrated trace functional \(H\), not the maximum real-part spectral gap or total-variation mixing time; these may order networks differently. It considers a single added directed edge, holding the original rates fixed, and does not characterize multiple simultaneous shortcuts. The monotone sign of one-edge perturbations need not persist for general graphs. Searches and inspected references reduce but cannot eliminate the risk of an unindexed equivalent result. Independent mathematical audit has not been performed.

## References

1. Catral, Kirkland, Neumann and Sze, *The Kemeny Constant for Finite Homogeneous Ergodic Markov Chains* (2010), full open text: https://mural.maynoothuniversity.ie/id/eprint/2185/1/SK_kemeny0209_revised.pdf (public repository deposit verified October 13, 2010).
2. Kirkland, *Fastest Expected Time to Mixing for a Markov Chain on a Directed Graph* (2010), full open text: https://www.hamilton.ie/skirkland/min_kemeny_final.pdf, DOI:10.1016/j.laa.2010.07.016.
3. Hunter, *The Role of Kemeny's Constant in Properties of Markov Chains* (2012), https://arxiv.org/abs/1208.4716 (first arXiv version August 23, 2012).
4. Kirkland and Zeng, *Kemeny's Constant and an Analogue of Braess' Paradox for Trees* (2016), https://emis.de/ft/34491, DOI:10.13001/1081-3810.3222.
5. Patel, Agharkar and Bullo, *Robotic Surveillance and Markov Chains with Minimal Weighted Kemeny Constant* (2014/2015), https://motion.me.ucsb.edu/pdf/2014b-pab.pdf, DOI:10.1109/TAC.2015.2426317.
