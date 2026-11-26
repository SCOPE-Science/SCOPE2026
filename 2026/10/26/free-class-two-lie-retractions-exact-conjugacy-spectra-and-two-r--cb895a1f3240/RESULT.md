# Two adjacent ranks are necessary for concentration of free class-two Lie retractions

## Finding

Let \(L_n=V\oplus\bigwedge^2 V\), where \(V=\mathbb F_q^n\), \(n\ge3\), and the bracket of two elements is the wedge of their projections to \(V\). Choose uniformly from the \(\mathbb F_q\)-linear Lie endomorphisms \(F\) of \(L_n\) satisfying \(F^2=F\). Let \(J_n\) be the rank induced on the abelianization \(V\), not the ordinary linear rank on \(L_n\). Write
\[
 S_n=\sqrt{7n^2+8n+4},\qquad t_n=(n-2+S_n)/6,\qquad k_n=\lfloor t_n\rfloor,
 \qquad C_q=\prod_{j\ge1}(1-q^{-j})^{-1}.
\]
For every \(n\ge3\),
\[
 \Pr(J_n\notin\{k_n,k_n+1\})\le (n+1)C_q q^{7-S_n/2}.
\]
For each fixed \(q\), there is an explicit infinite sequence of \(n\) on which \(\Pr(J_n=k_n)\to1/2\) and \(\Pr(J_n=k_n+1)\to1/2\). In particular no choice of a single deterministic rank for each \(n\) can replace the two-rank window with probability tending to one as \(n\to\infty\). The construction starts at \((n,m)=(24,65)\) and iterates
\[
 (n,m)\longmapsto(8n+4+3m,\ 21n+12+8m).
\]
In the full sequence of dimensions, \(J_n/n\to(1+\sqrt7)/6\) in probability for fixed \(q\).

## Proof

**Input: the exact finite-field rank enumerator.** The orbit classification and labeled idempotent count are known [1]; they are not claimed as new here. The rank-\(r\) weight from that count is
\[
 W_{n,q}(r)={n\brack r}_q q^{r(n-r)(n+2r)/2}.
\]
For completeness this weight follows by writing \(F(v+z)=Av+Bv+(\bigwedge^2 A)z\). The quotient map \(A\) must be a projection. With \(U=\operatorname{im}A\), \(K=\ker A\), \(C=\bigwedge^2 A\), idempotence is equivalent to \(B(U)\subseteq\ker C\) and \(B(K)\subseteq\operatorname{im}C\). For \(\dim U=r\), choosing \(U,K\) gives \({n\brack r}_q q^{r(n-r)}\) possibilities and choosing \(B\) gives \(q^{r(\binom n2-\binom r2)+(n-r)\binom r2}\). Multiplying and simplifying gives the stated weight, in any characteristic.

**Two-rank bound.** Write \(W_{n,q}(r)=q^{E_n(r)}c_{n,q}(r)\), where
\[
 E_n(r)=-r^3+(n/2-1)r^2+(n^2/2+n)r,
 \qquad
 c_{n,q}(r)=\frac{\prod_{j=n-r+1}^{n}(1-q^{-j})}{\prod_{j=1}^{r}(1-q^{-j})}.
\]
Termwise comparison shows \(1\le c_{n,q}(r)\le C_q\). The derivative of \(E_n\) is positive to the left of \(t_n\) and negative to its right on \([0,n]\); \(0<t_n<n\) since the derivative changes sign once there. Exactly,
\[
 E_n(t_n+s)=E_n(t_n)-S_n s^2/2-s^3.
\]
Writing \(\theta=t_n-k_n\in[0,1)\), the left gap \(E_n(k_n)-E_n(k_n-1)\) is \(S_n(1+2\theta)/2-(1+3\theta+3\theta^2)\ge S_n/2-7\). The right gap \(E_n(k_n+1)-E_n(k_n+2)\) is \(S_n(3-2\theta)/2+(7-9\theta+3\theta^2)\ge S_n/2+1\). Omit a gap if the outside index is not in \([0,n]\). Monotonicity bounds every outside term by \(C_q q^{7-S_n/2}\) times \(q^{\max(E_n(k_n),E_n(k_n+1))}\). The denominator of the normalized weights is at least the latter power; summing gives the bound. The convergence of \(J_n/n\) follows from \(t_n/n\to(1+\sqrt7)/6\).

**A subsequence where both ranks are needed.** The exact forward difference is
\[
 E_n(r+1)-E_n(r)=-3r^2+(n-5)r+(n^2+3n-4)/2.
\]
Its positive root is \((n-5+m)/6\) when \(m=\sqrt{7n^2+8n+1}\). With \(x=7n+4\), this square condition reads \(x^2-7m^2=9\). The seed \((24,65)\) satisfies it and \(n+m\equiv5\pmod6\). Multiplication of \(x+m\sqrt7\) by \(8+3\sqrt7\), which has norm one, gives exactly the displayed iteration. It sends \(n+m\) to \(29n+11m+16\equiv5(n+m)+4\equiv5\pmod6\), preserves positivity, and increases \(n\) without bound. Consequently \(r=(n-5+m)/6\) is an integer throughout. For \(n\ge24\), \(m<3n\), so \(r,r+1\in[0,n]\). Equality of \(E_n(r)\) and \(E_n(r+1)\) and strict increase/decrease imply \(r<t_n<r+1\), hence \(r=k_n\). As both \(r\) and \(n-r\) tend to infinity, \(c_{n,q}(r)\) and \(c_{n,q}(r+1)\) both tend to \(C_q\): the denominator products tend to \(C_q^{-1}\) and the numerator products tend to one. The ratio of the two weights therefore tends to one, while their combined probability tends to one by the bound. This proves the two limits of one half and the necessity of two ranks.

## Scope and relationship to prior work

The rank law concerns uniform labeled retraction maps of the free class-two **Lie** algebra, not a uniform sample of their image subalgebras or a group-theoretic analogue. The optimality assertion is for fixed \(q\) and varying generator number. It does not say that both ranks carry nonnegligible mass at every dimension, or that the displayed bound's numerical constants are optimal.

The earlier conjugacy and exact census [1] supply the weight, which is used as input. A class-dependent higher-class concentration result [2] concerns class \(c\ge3\) and a limiting generator proportion; it does not give the class-two two-point obstruction. The two-rank upper bound is included for context; the distinct assertion is the explicit infinite subsequence on which the two adjacent ranks have asymptotically equal mass. The discrete equal-exponent condition, not the continuous saddle location by itself, is what detects that obstruction.

## References

1. *Retraction orbits and finite-field rank spectra of free two-step nilpotent Lie algebras*, [result](https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-retraction-orbits-and-finite-field-rank-spectra-of-free-two-step--7573f7956962/RESULT.md).
2. *Retraction-rank spectra and class-dependent concentration in free nilpotent Lie algebras*, [result](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-retraction-rank-spectra-and-class-dependent-concentration-in-fre--3c25041b20ac/RESULT.md).
