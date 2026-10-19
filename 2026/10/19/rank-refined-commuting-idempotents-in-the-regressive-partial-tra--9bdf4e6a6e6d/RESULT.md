# Rank-refined commuting idempotents in the regressive partial transformation monoid

## Finding
For each integer \(n\geq0\), let \(P_n\) consist of all partial maps on the chain \([n]=\{1,\ldots,n\}\) that preserve order on their domains and satisfy \(e(i)\leq i\) wherever defined. Denote the set of its idempotents by \(E_n\). If \(e,f\in E_n\) commute, then \(ef\) is idempotent. Let \(c_{n,k}\) count ordered commuting pairs for which \(\operatorname{rank}(ef)=k\).

The full rank-refined ordinary generating function is
\[
F(z,y)=\sum_{n\geq0}\sum_{k=0}^{n}c_{n,k}z^ny^k
=\frac{(1-4z)(1-7z+8z^2)}{(1-z)[1-(13+y)z+(54+7y)z^2-(72+8y)z^3]}.
\]
In particular, define
\[
Z(z)=\frac{1-7z+8z^2}{(1-z)(1-3z)(1-6z)},\quad
H(z)=\frac{1-7z+8z^2}{(1-3z)(1-4z)(1-6z)}.
\]
Then for every \(k\geq0\),
\[
\sum_{n\geq k} c_{n,k}z^n=z^k Z(z)H(z)^k,
\quad F(z,y)=\frac{Z(z)}{1-yzH(z)}.
\]
The product-rank-zero counts have a simple exact form:
\[
c_{n,0}=\frac{3+10\cdot3^n+2\cdot6^n}{15}.
\]
The total numbers of pairs for \(n=0,1,\ldots,7\) are \(1,4,21,124,769,4876,31269,201844\). The first four nontrivial rank-polynomials are
\[
\begin{aligned}
C_1(y)&=3+y,\\
C_2(y)&=11+9y+y^2,\\
C_3(y)&=47+61y+15y^2+y^3,\\
C_4(y)&=227+373y+147y^2+21y^3+y^4.
\end{aligned}
\]

## Assumptions and scope
All maps are partial functions, not total functions. Order preservation compares points belonging to the domain; an undefined value is represented by \(0\) only in calculations, not as an ordered point of the domain. The empty map is allowed. Products are composition; since the counted pairs commute, their order of composition does not affect the answer. The empty chain contributes \(c_{0,0}=1\). All identities are formal, valid over the integers without field or characteristic assumptions.

For an idempotent \(e\), its image equals its fixed-point set \(A\). At each index \(i\in A\), \(e(i)=i\). At any other index \(i\), the map is either undefined or takes the largest \(a\in A\) below \(i\) (if such an \(a\) exists). Indeed every defined value is fixed, and order preservation against the largest earlier fixed point forces the value to be that point. Conversely all such choices give idempotents in \(P_n\). In particular, \(|E_n|=(3^n+1)/2\).

## Proof
**Local commutation condition.** Regard undefined map values as \(0\) and set \(e(0)=f(0)=0\) for the sole purpose of computing compositions. Immediately before an index \(i\), let \(a,b\) denote the last fixed point, if any, of \(e,f\), respectively; put \(u=f(a)\) and \(v=e(b)\), with \(u=0\) when \(a\) does not exist and \(v=0\) when \(b\) does not exist. For an index which is fixed by neither map, there are four possible patterns of definedness (subject to the existence of \(a,b\)). Both undefined always commutes; only \(e\) defined is permitted exactly when \(u=0\); only \(f\) defined exactly when \(v=0\); and both defined exactly when \(u=v\). This follows by evaluating \(f(e(i))=e(f(i))\). If only \(e\) gains a fixed point, \(f(i)\) can be undefined; it can instead equal \(b\) only when \(b\) is a common fixed point. The symmetric rule holds if only \(f\) gains a fixed point. If both become fixed at \(i\), the new common point erases dependence on all earlier fixed points. These cases exhaust every idempotent pair.

A common fixed point of \(e,f\) is exactly a fixed point of their commuting product. To see the reverse implication, use \(e(f(i))\leq f(i)\leq i\): equality to \(i\) forces \(f(i)=i\) and \(e(i)=i\). Thus the exponent of \(y\) marks precisely the number of common-fixed-point events.

**Prefix before the first common fixed point.** In a segment having no common fixed point, every cross-value \(u,v\) must be \(0\). There are three state types: neither map has yet acquired a fixed point, exactly one has, and both have (at distinct points). Let their remaining-suffix series be \(Z,U,P\), respectively. Directly applying the local rule, while forbidding new common fixed points, gives
\[
P=1+6zP,\qquad U=1+z(3U+P),\qquad Z=1+z(Z+2U).
\]
The six continuations in state \(P\) are the four definedness patterns with neither new fixed point and the two ways of gaining an exclusive fixed point. Solving gives
\[
P=\frac1{1-6z},\quad U=\frac{1-5z}{(1-3z)(1-6z)},\quad
Z=\frac{1-7z+8z^2}{(1-z)(1-3z)(1-6z)}.
\]

**Segment after a common fixed point.** Start immediately after a common fixed point and forbid any further common fixed point. Whenever either map has a new exclusive fixed point, its cross-value under the other map is either \(0\) or that most recent common fixed point. If both maps have an exclusive last fixed point, the possible pairs of cross-values are \((0,0),(0,h),(h,0)\), never \((h,h)\). Write \(P\) for the \((0,0)\) state, \(Q\) for either one-nonzero state, \(X_0,X_1\) for the states where one latest fixed point is exclusive and the other is common, with the exclusive cross-value equal to \(0,h\) respectively, and \(H\) for the initial common/common state. Direct continuation counts are
\[
\begin{aligned}
P&=1+6zP,\\
Q&=1+z(3Q+P),\\
X_0&=1+z(3X_0+X_1+P),\\
X_1&=1+z(X_0+3X_1+Q),\\
H&=1+z(2H+2X_0+2X_1).
\end{aligned}
\]
The factor \(2\) in the last equation for a non-fixed index counts either both maps undefined or both mapping to the current common fixed point. The other two terms have symmetric choices of which map receives the new exclusive fixed point. The preceding local rule verifies every transition. Setting \(S=X_0+X_1\), we obtain \(S=(2+z(P+Q))/(1-4z)\) and \(H=(1+2zS)/(1-2z)\). Substitution yields
\[
H(z)=\frac{1-7z+8z^2}{(1-3z)(1-4z)(1-6z)}.
\]

**Renewal at common fixed points.** Every commuting pair has a unique decomposition into an initial no-common prefix, followed by \(k\) common fixed points, each followed by a no-common suffix. Once a common fixed point occurs, the local rules reset, so lengths add and the choices of successive segments are independent. Consequently the rank-\(k\) generating series is \(z^kZ(z)H(z)^k\). Summing the geometric series gives \(F(z,y)=Z(z)/(1-yzH(z))\) and the claimed displayed rational function. A partial-fraction decomposition of \(Z\) gives the exact formula for \(c_{n,0}\). Setting \(y=1\) gives the unrefined total generating function
\[
F(z,1)=\frac{(1-4z)(1-7z+8z^2)}{(1-z)(1-5z)(1-9z+16z^2)}.
\]
This completes the argument for every \(n,k\).

## Verification
Run \(\texttt{python3 verify.py}\) using standard Python 3. The program independently constructs all idempotent partial regressive order-preserving maps for \(0\leq n\leq7\), exhaustively evaluates commutation and product ranks for every ordered pair, and compares against the rational generating function. A separate twelve-state transfer recursion checks the same bivariate rational coefficients through \(n=16\). The packaged program reports \(\texttt{VERIFY\_OK}\) on success. The symbolic proof above, not finite enumeration, establishes the infinite statement.

## Relationship to prior work
Zhao, You, Xu and Hu (2011) study the same semigroup \(P_n\) and its idempotent rank and generation. These properties do not imply the rank distribution of commuting ordered pairs. Fernandes (2008) studies pseudovarieties of normally ordered block-groups and partial injective order-preserving actions, including general properties of idempotent-commuting semigroups, rather than enumerating commuting pairs in the noninjective order-decreasing partial semigroup. Ganyushkin and Mazorchuk (2010) connect Hecke–Kiselman monoids and *total* Catalan transformations; this is not a formula for partial-domain commuting pairs. Existing total Catalan idempotent-pair product-fiber formulas concern a strict full-domain submonoid, and partial-involution formulas concern a different family. The present bivariate series cannot be obtained by simply relabeling either result: for example the number of pairs at \(n=4\) here is \(769\), while the corresponding partial-involution count is \(817\).

## Limitations
This theorem counts pairs by rank of their product, not by individual prescribed product maps; it does not classify all idempotent-generated subsemigroups. It does not assert absolute literature uniqueness. The 2011 primary publication's bibliographic page and abstract were accessible, but its full article was not retrieved; possible stronger results inside it are a residual literature risk. No independent mathematical audit has been performed.

## References
1. Zhao, P.; You, T.; Xu, B.; Hu, H., *Idempotent rank in decreasing and order-preserving finite partial transformation semigroups*, Journal of Shandong University (Natural Science) **46** (2011), 75–77; public record dated 2011-04-21. https://lxbwk.njournal.sdu.edu.cn/EN/Y2011/V46/I4/75
2. Fernandes, V. H., *Normally ordered semigroups*, Glasgow Mathematical Journal **50** (2008), 325–333. https://doi.org/10.1017/S0017089508004230 ; freely accessible text: https://run.unl.pt/bitstream/10362/5532/1/Fernandes_2008.pdf
3. Ganyushkin, O.; Mazorchuk, V., *On Kiselman quotients of 0-Hecke monoids*, International Electronic Journal of Algebra **10** (2011), 174–191, initial arXiv submission 2010-06-02. https://arxiv.org/abs/1006.0316
