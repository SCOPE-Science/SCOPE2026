# A single curvature reversal for heterogeneous geometric maxima and the sharp four-point threshold

## Finding

Let \(X\) and \(Y\) be independent geometric random variables supported on \(\{0,1,2,\ldots\}\), with \(\Pr(X=k)=(1-r)r^k\) and \(\Pr(Y=k)=(1-s)s^k\), for \(0<r,s<1\). Write \(p_k=\Pr(\max(X,Y)=k)\) and \(\Delta_k=p_k^2-p_{k-1}p_{k+1}\) for integers \(k\ge1\).

**Exact sign-transition theorem.** If \(r=s\), then \(\Delta_k>0\) for every integer \(k\ge1\). If \(r\ne s\), there is a unique real number \(\kappa(r,s)>1\) such that \(\Delta_k>0\) for \(1\le k<\kappa(r,s)\), \(\Delta_k<0\) for \(k>\kappa(r,s)\), and equality is possible only if \(k=\kappa(r,s)\) is an integer. In particular, the law of \(\max(X,Y)\) is log-concave if and only if \(r=s\). Furthermore,
\[
\lim_{k\to\infty}\frac{\Delta_k}{(rs)^{k-1}}
=-(1-r)(1-s)(r-s)^2.
\]

**Sharp finite-support boundary.** The maximum of any two independent, strictly positive, log-concave laws sharing a consecutive three-point support is log-concave. The assertion fails on a common consecutive four-point support: normalized weights proportional to \((1,r,r^2,r^3)\) and \((1,s,s^2,s^3)\), for \(r=1/10\) and \(s=1/5\), give \(\Delta_2<0\). Thus four is the least common contiguous support size admitting a failure.

## Assumptions and scope

Here a nonnegative sequence \((p_k)\) is log-concave when \(p_k^2\ge p_{k-1}p_{k+1}\) at every interior index. Both geometric parameters belong to \((0,1)\), so all masses are strictly positive. The real threshold \(\kappa\) concerns the sign of the discrete curvature at integral indices; it is not a mode location. The finite-support assertion requires independent parents with strictly positive masses on the same three (respectively four) consecutive integer sites; a translation of sites is immaterial.

## Proof

**Step 1: probability mass.** Independence and the two geometric CDFs yield
\[
\Pr(\max(X,Y)\le k)=(1-r^{k+1})(1-s^{k+1}),
\quad
p_k=(1-r)r^k+(1-s)s^k-(1-rs)(rs)^k.
\]
Put \(A=1-r\), \(B=1-s\), and \(C=1-rs\). For an exponential sum \(u_k=\sum_i a_i t_i^k\), direct expansion gives the exact pairwise identity
\[
u_k^2-u_{k-1}u_{k+1}
=-\sum_{i<j}a_i a_j(t_i-t_j)^2(t_i t_j)^{k-1}.
\]
Apply it to the three terms \((A,r)\), \((B,s)\), and \((-C,rs)\). For every integer \(k\ge1\),
\[
\Delta_k=(rs)^{k-1}H(k),\quad
H(t)=-AB(r-s)^2+AC(1-s)^2r^{t+1}+BC(1-r)^2s^{t+1}.
\]
This algebra is also independently checked by the accompanying exact-symbolic program.

**Step 2: one sign reversal.** All positive-term coefficients of \(H(t)\) are strictly positive, and \(\log r<0\), \(\log s<0\). Hence \(H(t)\) is strictly decreasing on \([1,\infty)\). At the first index, factorization gives
\[
H(1)=rs(1-r)^2(1-s)^2(r+s+2)>0.
\]
If \(r\ne s\), then \(H(t)\to-AB(r-s)^2<0\), so strict monotonicity and continuity give a unique root \(\kappa(r,s)>1\) and the stated exact sign classification at integer \(k\). The negative limiting curvature and the non-log-concavity follow. If \(r=s=t\), the two coinciding bases can be combined; the same pairwise identity yields
\[
\Delta_k=2t^2(1-t)^4(1+t)t^{3(k-1)}>0
\qquad(k\ge1).
\]
This proves the infinite-support theorem, including the equality case and asymptotic normalization.

**Step 3: all positive three-point parents.** Translation lets the common support be \(\{0,1,2\}\). Up to individual positive normalizing constants write the two parents as \((1,u,v)\) and \((1,w,z)\), with \(u,w,v,z>0\). Their log-concavity implies \(v\le u^2\) and \(z\le w^2\). The unnormalized maximum weights are
\[
c_0=1,\quad c_1=u+w+uw,\quad
c_2=v(1+w+z)+z(1+u).
\]
Since \(c_2\) is increasing in each of \(v,z\),
\[
c_1^2-c_0c_2\ge
(u+w+uw)^2-u^2(1+w+w^2)-w^2(1+u)
=uw(u+w+2)>0.
\]
Common normalization divides this difference by a positive square, preserving its sign. There is no further interior log-concavity condition for a three-point sequence.

**Step 4: an exact four-point violation.** On \(\{0,1,2,3\}\), take positive parents with weights proportional to \((1,r,r^2,r^3)\) and \((1,s,s^2,s^3)\). Their adjacent log-concavity inequalities are equalities. Before normalization, the maximum has masses
\[
c_1=r+s+rs,\quad
c_2=r^2(1+s+s^2)+s^2(1+r),\quad
c_3=r^3(1+s+s^2+s^3)+s^3(1+r+r^2).
\]
Direct expansion gives
\[
c_2^2-c_1c_3
=rs\left[rs(r^2+s^2+r+s+2)-(r^2+s^2)\right].
\]
At \(r=1/10\), \(s=1/5\), this equals \(-3/50000\). If \(Z_t=1+t+t^2+t^3\), the normalized curvature is \(-3/(50000Z_r^2Z_s^2)<0\), proving the sharp four-point boundary.

## Verification

Run `python checker.py` with Python 3 and SymPy installed. The program checks the exponential-pair curvature identity by symbolic expansion at six different integral indices, the two finite-support polynomial factorizations, the exact value \(-3/50000\), and four hundred exact-rational parameter/index identities and sign diagnostics. All checks passed on the supplied source. The proof of strict monotonicity and uniqueness for unbounded \(k\) is analytical, not inferred from those finite checks.

## Relationship to prior work

Badiella, del Castillo, and Puig (2023) prove preservation of log-concavity and ultra-log-concavity for order statistics formed from an **identically distributed** discrete sample. Their Theorem 2 is a genuine preservation theorem but assumes one common parent mass function; it therefore does not imply preservation for distinct geometric parents or classify the opposite-sign transition. Earlier papers of Alimohammadi, Alamatsaz, and Cramer (2015) and Kim, Kim, and Lee (2018) also develop log-concavity for discrete order statistics; the available abstracts concern order statistics from one strongly unimodal distribution. Related discrete geometric/log-concave extremal literature addresses entropy rather than this maximum's curvature.

The sharp three-versus-four-point boundary and the unique curvature crossover are specific to the present statement, not consequences of identical-parent closure. Full texts of the 2015 and 2018 articles were not available for direct inspection; no absolute priority claim is made. An equivalent earlier formulation remains a residual possibility.

## Limitations

The explicit single-switch classification concerns exactly two independent geometric parents. It does not classify maxima of three or more heterogeneous parents or arbitrary log-concave inputs. The support-cardinality threshold concerns parents on the **same consecutive finite support**. An equality at an integer transition index is possible but not classified by closed elementary parameter formulas. A finding of no equivalent literature during the searches is not proof of bibliographic uniqueness; independent review has not occurred.

## References

1. L. Badiella, J. del Castillo, P. Puig, “Ultra log-concavity of discrete order statistics,” *Statistics & Probability Letters* **201** (2023), 109900, DOI: `10.1016/j.spl.2023.109900`. Open full text: https://ddd.uab.cat/pub/artpub/2023/283158/StaProLet_a2023v201n109900.pdf . First public availability stated as 26 June 2023.
2. M. Alimohammadi, M. H. Alamatsaz, E. Cramer, “Discrete strong unimodality of order statistics,” *Statistics & Probability Letters* **103** (2015), 176–185, DOI: `10.1016/j.spl.2015.04.019`.
3. B. Kim, J. Kim, S. Lee, “Strong unimodality of discrete order statistics,” *Statistics & Probability Letters* **140** (2018), DOI: `10.1016/j.spl.2018.04.018`.
4. J. Jakimiuk, D. Murawski, P. Nayar, S. Słobodianiuk, “Log-concavity and discrete degrees of freedom,” arXiv:`2205.04069` (2022); unrelated geometric entropy extremals provide additional background.
