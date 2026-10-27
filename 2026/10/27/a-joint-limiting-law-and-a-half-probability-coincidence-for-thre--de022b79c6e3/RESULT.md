# A joint limiting law and a half-probability coincidence for three overpartition minimal excludants

## Finding
For a uniformly random overpartition \(\pi\) of \(n\), let \(A_n\) be the smallest positive size missing from all parts, \(B_n\) the smallest missing from its nonoverlined parts, and \(C_n\) the smallest missing from its overlined parts. The three statistics refer to the same sampled overpartition. Let \(T_0,T_1\) be independent positive random variables with \(\Pr(T_i>x)=\exp(-\pi x^2/8)\) for \(x\ge0\), and let \(G\) be independent of them with \(\Pr(G>k)=2^{-k}\) for every integer \(k\ge0\). Then, as \(n\to\infty\),
\[
(C_n,\, n^{-1/4}B_n,\, n^{-1/4}A_n)\ \Longrightarrow\ (G,\,\min(T_0,T_1),\,T_0).
\]
In particular, for fixed nonnegative \(x,y\) and integer \(k\ge0\),
\[
\Pr(C_n>k,\ B_n>x n^{1/4},\ A_n>y n^{1/4})
\longrightarrow 2^{-k}\exp\!\left(-\frac{\pi}{8}\bigl(x^2+\max(x,y)^2\bigr)\right).
\]
There is also a stronger exact-integer coincidence conclusion not implied by weak convergence alone:
\[\Pr(A_n=B_n)\longrightarrow\frac12.\]
For \(0\le r<1\), the ratio satisfies
\[
\Pr(B_n/A_n\le r)\longrightarrow\frac{r^2}{1+r^2},
\]
while \(\Pr(B_n/A_n=1)\to1/2\).

## Assumptions and scope
An overpartition is a finite integer partition in which at most one occurrence of each positive size may be overlined. Only the three specifically defined presence-based minimal excludants are considered, not mex under a combined ordered alphabet of marked and unmarked symbols. The sample space is all overpartitions of each integer \(n\ge1\), equally weighted. Every limiting parameter \(k,x,y,r\) in the formulas is fixed as \(n\to\infty\). Neither growing-parameter uniformity nor pointwise rates are asserted.

## Proof
Write \(F(q)=\prod_{j\ge1}(1+q^j)/(1-q^j)=\sum_{n\ge0}\overline p(n)q^n\). At a part size \(j\), the unrestricted local factor is \((1+q^j)/(1-q^j)\). Constraining this size to have a nonoverlined part replaces the factor by \(q^j(1+q^j)/(1-q^j)\), hence multiplies \(F\) by \(q^j\). Requiring some part, marked or not, gives \(2q^j/(1-q^j)\), hence local multiplier \(2q^j/(1+q^j)\). Forcing complete absence gives multiplier \((1-q^j)/(1+q^j)\). Therefore, for integers \(a,b\ge0\), the joint tail enumerator is exactly
\[
\sum_{\pi:B(\pi)>a,\ A(\pi)>b}q^{|\pi|}
=F(q)q^{a(a+1)/2}\prod_{j=a+1}^{\max(a,b)}\frac{2q^j}{1+q^j}.
\tag{1}
\]
(The empty product equals one.) Define \(t_n>0\) by \(-d\log F(e^{-t})/dt|_{t=t_n}=n\). The standard eta-product expansion of \(F(e^{-t})\) is
\[
\log F(e^{-t})=\frac{\pi^2}{4t}+\frac12\log t-\log(2\sqrt\pi)+O(t),
\]
so \(t_n=\pi/(2\sqrt n)+O(n^{-1})\), and its Boltzmann size variance is \(4n^{3/2}/\pi\,(1+o(1))\). We use the following local transfer fact for these exact restrictions: if finitely many choices of presence/absence/marking are imposed only at sizes \(j\le L n^{1/4}\), and their total local weight generating function relative to \(F\) is \(H_n(q)\), then, whenever \(H_n(e^{-t_n})>0\) and grows or decays at most polynomially,
\[
\frac{[q^n]F(q)H_n(q)}{[q^n]F(q)}=H_n(e^{-t_n})(1+o(1)). \tag{2}
\]
Here and below, the \(o(1)\) is uniform over bounded integer cutoffs \(a,b\le L n^{1/4}\) for the specific restrictions used. To verify (2), use Cauchy's coefficient integral at \(|q|=e^{-t_n}\). The logarithm of the unrestricted characteristic function for \(|\theta|\le n^{-3/4+1/20}\) equals \(-\frac12(4n^{3/2}/\pi)(1+o(1))\theta^2+O(n^2|\theta|^3)\); on its effective Gaussian window \(|\theta|=O(n^{-3/4})\), the normalized finite local constraints have logarithmic derivatives \(O(\sqrt n)\) in the angular variable and so contribute \(1+o(1)\). In the complementary arcs, the untouched block \(\sqrt n\le j\le2\sqrt n\) gives a factor at most \(\exp[-c\min(\sqrt n,n^{3/2}\theta^2)]\) by the formula for the modulus of \((1+q^j)/(1-q^j)\) and the bound \(\sum_{\sqrt n\le j\le2\sqrt n}\sin^2(j\theta/2)\gg\min(\sqrt n,n^{3/2}\theta^2)\), for \(|\theta|\le\pi\). Each restricted small-size numerator has nonnegative coefficients, so its modulus never exceeds its positive-real value; a polynomial loss from division by \(H_n(e^{-t_n})\) is dominated by this exponential. This yields (2), including the one-missing-size case where \(H_n(e^{-t_n})\asymp n^{-1/4}\). The stated derivative bound follows by direct differentiation of the local factors: \(O(n^{1/4})\) factors of sizes at most \(L n^{1/4}\) each contribute \(O(n^{1/4})\), while a single forced absence contributes \(O(1/t_n)\). This establishes the necessary uniform estimates without assuming independent part sizes after conditioning on \(n\).

For \(a=\lfloor x n^{1/4}\rfloor\) and \(b=\lfloor y n^{1/4}\rfloor\), the logarithm of the right-hand local factor of (1) evaluated at \(e^{-t_n}\) equals
\[
-\frac{t_n a(a+1)}2-\frac{t_n}2\sum_{j=a+1}^{\max(a,b)}j+o(1)
\ \longrightarrow\ -\frac\pi8\bigl(x^2+\max(x,y)^2\bigr).
\]
The transfer (2) proves the joint tail law for \((B_n,A_n)\), identifying it with \((\min(T_0,T_1),T_0)\). For each fixed \(k\ge0\), insisting that all sizes \(1,\ldots,k\) have an overlined occurrence has asymptotic conditional probability \(2^{-k}\) under the previous first-gap constraints: the overline probability at any fixed size \(j\), given its presence under either nonoverlined-required or any-present restrictions, is \(e^{-t_n j}/(1+e^{-t_n j})\to1/2\) or exactly \(1/2\), respectively; for an otherwise unconstrained size the probability is also \(e^{-t_nj}/(1+e^{-t_nj})\to1/2\). Applying (2) to the finite marking constraints establishes independence of the geometric limit \(G\). Tail probabilities characterize the weak limit, since the continuous pair is tight by its displayed tails and the discrete coordinate has summable tails.

For the exact coincidence, \(A_n=B_n=j\) precisely if each size below \(j\) has a nonoverlined part and size \(j\) is completely absent. Its exact enumerator is
\[
F(q)\,q^{j(j-1)/2}\frac{1-q^j}{1+q^j}.\tag{3}
\]
Uniformly for \(j\le L n^{1/4}\), (2) and the local Taylor expansion yield a local mass with absolute error \(o(n^{-1/4})\), and for \(j/n^{1/4}\to z\) its main term is
\[
n^{-1/4}\frac{\pi z}{4}\exp(-\pi z^2/4).
\]
The Riemann-sum limit for \(j\le Ln^{1/4}\) is \(\int_0^L(\pi z/4)e^{-\pi z^2/4}\,dz\). The remaining probability for \(j>Ln^{1/4}\) is bounded by \(\Pr(B_n>Ln^{1/4})\to e^{-\pi L^2/4}\), so letting \(L\to\infty\) gives precisely \(1/2\). Finally \(B_n/A_n\Rightarrow\min(1,T_1/T_0)\), as \(T_0>0\) almost surely. The ratio CDF for \(r<1\) is \(r^2/(1+r^2)\) by integrating two independent Rayleigh densities; the point mass at one follows from the separately established exact coincidence probability.

## Verification
The included `verify.py` uses an independent recurrence for unrestricted overpartition numbers and exhaustive enumeration of marked partitions through \(n=11\) to check the exact joint generating function (1), the coincidence enumerator (3), and the inequality \(B_n\le A_n\). It also computes exact coincidence frequencies at \(n=100,400,900\), respectively \(0.61871280\), \(0.58580685\), and \(0.57059225\), and checks joint-tail probabilities at \(n=400\) against the explicit saddle factors. Running `python3 verify.py` prints `VERIFY_OK`. These finite tests do not replace the limiting analytic argument above.

## Relationship to prior work
Aricheta--Donato (2024) treat the nonoverlined mex and its individual sums, Donato (2025) defines the overlined and all-part alternatives and establishes separate generating functions and summatory asymptotics, and Dhar--Mukhopadhyay--Sarma (2024/2025) give different mex variants and \(q\)-series identities. Veena--Fathima (2026) study an odd-restricted aggregate of the all-part mex. The current joint weak limit, the macroscopic diagonal atom, and the separate literal equality probability compare the three existing conventions on the *same* overpartition; none of the inspected theorem statements supplies their joint law. Ordinary-partition residue-class first gaps obey a different probability model and do not directly imply this result.

## Limitations
No effective rate of convergence is claimed. The theorem concerns uniformly sampled unrestricted overpartitions and three presence-based mex definitions, not ordered marked-alphabet mex or restrictions to odd-part overpartitions. Similar results could follow implicitly from a broader partition limit theorem, and bibliographic priority beyond the inspected works has not been independently established. 

## References
1. V. M. R. Aricheta and J. A. L. Donato, *A Minimal Excludant over Overpartitions*, Journal of Integer Sequences **27** (2024), article 24.7.1, https://cs.uwaterloo.ca/journals/JIS/VOL27/Donato/donato15.html.
2. J. A. L. Donato, *On Minimal Excludant over Overpartitions*, arXiv:2507.04402 (first posted July 2025), https://arxiv.org/abs/2507.04402.
3. A. Dhar, A. Mukhopadhyay and R. Sarma, *On new minimal excludants of overpartitions related to some q-series of Ramanujan*, arXiv:2409.06121 (first posted September 2024), https://arxiv.org/abs/2409.06121.
4. V. V. S. and S. N. Fathima, *On the sum of odd minimal excludants over overpartitions*, arXiv:2609.32207 (first posted September 26, 2026), https://arxiv.org/abs/2609.32207.
