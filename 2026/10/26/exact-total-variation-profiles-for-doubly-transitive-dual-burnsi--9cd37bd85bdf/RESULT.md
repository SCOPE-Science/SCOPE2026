# Exact total-variation profiles for doubly transitive dual Burnside walks

## Finding
Let a finite group \(G\) act doubly transitively on a set \(X\) of cardinality \(n\ge3\). Write \(f(g)=|\operatorname{Fix}_X(g)|\), \(G^*=\{g:f(g)>0\}\), and \(H=G_x\) for any point stabilizer. The dual Burnside kernel \(Q\) first selects a uniform point fixed by its current group element and then a uniform element of that point stabilizer. Put
\[
a=\frac1{|H|}\sum_{h\in H}\frac1{f(h)},\qquad \lambda=\frac{na-1}{n-1}.
\]
Then \(0<\lambda<1\), the invariant distribution is \(\pi(h)=f(h)/|G|\), and for every \(g\in G^*\) and every integer \(t\ge1\),
\[
Q^t(g,h)=\pi(h)+\lambda^{t-1}\bigl(Q(g,h)-\pi(h)\bigr)\quad(h\in G^*).
\]
Consequently \(d_{\mathrm{TV}}(Q^t(g,\cdot),\pi)=\lambda^{t-1}d_{\mathrm{TV}}(Q(g,\cdot),\pi)\) *exactly*, not just asymptotically. If the action contains an element fixing exactly one point, then the sharp worst-start profile is
\[
\boxed{\sup_{g\in G^*}d_{\mathrm{TV}}(Q^t(g,\cdot),\pi)=\Bigl(1-\frac2n\Bigr)\lambda^{t-1}\quad(t\ge1).}
\]
Two explicit families with exactly the same sharp first-step discrepancy behave differently:
\[
\lambda(S_n\curvearrowright[n])=\frac{n\sum_{j=1}^n(-1)^{j-1}/j!-1}{n-1}\longrightarrow1-e^{-1};
\]
\[
\lambda(\operatorname{AGL}(1,q)\curvearrowright\mathbb F_q)=\frac{q-2}{q-1},\qquad q\ge3\text{ a prime power}.
\]
Thus the first family has uniformly bounded relaxation time while the second has relaxation time of order \(q\). The exact total-variation mixing times are obtained by solving \((1-2/n)\lambda^{t-1}\le\varepsilon\) for integers \(t\ge1\). For every *transitive* action, a one-step projection to conjugacy classes is already stationary; this latter fact is a direct consequence of the earlier general orbit/conjugacy quotient theorem, and is included only to explain why conjugacy statistics cannot diagnose the slow affine-family mixing.

## Assumptions and scope
All groups and action sets are finite. The action is doubly transitive, not necessarily faithful. The dual walk runs on \(G^*\) and uses uniform choices in the two successive conditional sampling stages. The worst-start equality assumes at least one group element with exactly one fixed point; the fixed-start geometric decay requires no such extra hypothesis. For \(S_n\), assume \(n\ge3\). For the affine example, \(q\ge3\) is a prime power. The \(t\)-step identities are asserted only for integers \(t\ge1\), since at time zero the law is a point mass.

## Proof
**1. Factorization and the two-eigenvalue reduction.** Define \(A(g,x)=\mathbf1_{\{gx=x\}}/f(g)\), and \(B(x,h)=\mathbf1_{\{hx=x\}}/|G_x|\). Then \(Q=AB\); its companion \(K=BA\) on \(X\) satisfies \(K(x,y)=|H|^{-1}\sum_{h\in H}\mathbf1_{\{hy=y\}}/f(h)\) for \(x=y\) and, more generally, \(K(x,y)=|H|^{-1}\sum_{h\in H:\,hy=y}1/f(h)\). Because \(G_x\) is transitive on \(X\setminus\{x\}\), \(K(x,x)=a\) and every other entry in the same row is \((1-a)/(n-1)\). In matrix form \(K=\Pi+\lambda(I-\Pi)\), where \(\Pi\) is the matrix with every entry \(1/n\). Since \(K\) is symmetric and doubly stochastic, this identity holds in every row.

**2. Exact-time formula.** The elementary identity \(Q^t=A K^{t-1}B\) holds for integers \(t\ge1\). Since \(K^{t-1}=\Pi+\lambda^{t-1}(I-\Pi)\), we obtain \(Q^t=A\Pi B+\lambda^{t-1}(Q-A\Pi B)\). The row law of \(A\Pi B\) is uniform-point-then-uniform-stabilizer; for every \(h\in G^*\), it equals \(f(h)/(n|H|)=f(h)/|G|=\pi(h)\), by transitivity. This proves the exact affine interpolation. To see \(0<\lambda<1\), the point-stabilizer action has two orbits, so \(\mathbb E_{h\sim\mathrm{Unif}(H)}f(h)=2\). Jensen gives \(a\ge1/2>1/n\), while \(a<1\) because the identity fixes all \(n\) points. Therefore the interpolation coefficient is strictly between zero and one.

**3. Sharp worst start.** Let \(\mu_x\) denote the uniform probability on \(G_x\). Every one-step row of \(Q\) is a convex combination of the \(\mu_x\) with \(x\in\mathrm{Fix}(g)\). Since \(\pi(h)=f(h)/|G|\) and \(\mu_x(h)=n\mathbf1_{h\in H}/|G|\), one has \(\mu_x(h)\ge\pi(h)\) for \(h\in H\), while \(\mu_x(h)=0\) otherwise. Hence
\[
\|\mu_x-\pi\|_{\mathrm{TV}}=1-\pi(H)
=1-\frac1n\mathbb E_{h\sim\mathrm{Unif}(H)}f(h)=1-\frac2n.
\]
Convexity bounds each one-step distance by \(1-2/n\). If \(g\) fixes only \(x\), its one-step row is precisely \(\mu_x\), attaining the bound. Step 2 propagates this exact value through all positive times.

**4. Symmetric group.** For \(G=S_n\) on \([n]\), the stabilizer is \(S_{n-1}\). For uniform \(h\in H\), \(f(h)=1+J\), where \(J\) is the number of fixed points of a uniform permutation on \(n-1\) points. Its probability generating polynomial is \(\mathbb E[t^J]=\sum_{j=0}^{n-1}(t-1)^j/j!\). Integrating from zero to one and using \(1/(1+J)=\int_0^1 t^Jdt\),
\[
a=\sum_{j=0}^{n-1}\frac{(-1)^j}{(j+1)!}=\sum_{k=1}^n\frac{(-1)^{k-1}}{k!}.
\]
For \(n\ge3\), an \((n-1)\)-cycle fixing the remaining point provides a singleton fixed set. The alternating exponential series yields the stated limit for \(\lambda\).

**5. Affine group.** An element of \(\operatorname{AGL}(1,q)\) is \(z\mapsto uz+v\), with \(u\in\mathbb F_q^\times\). Its point stabilizer has \(q-1\) elements: the identity, which fixes \(q\) points, and \(q-2\) nonidentity dilations, each fixing only the base point. Thus \(a=((q-2)+1/q)/(q-1)=(q-1)/q\) and \(\lambda=(q-2)/(q-1)\). For \(q\ge3\), nonidentity dilations attain the sharp worst start. The group acts doubly transitively for every prime power \(q\).

## Verification
A standalone Python program, `verify_dual_burnside.py`, constructs exact transition matrices using rational arithmetic for \(S_3,S_4,S_5\) and affine groups of prime orders \(3,5,7\); it tests double transitivity, stationary masses, conjugacy-class projections, the two-step semigroup identity and sharp one-step total variation. It also checks the closed constants through \(n=19\) and \(q=49\). The output records **8,370 exact-rational equalities/assertions**. These finite checks do not prove the all-\(n\) theorem; the analytical proof above supplies that argument.

## Relationship to prior work
Feng (2025/2026) introduced the systematic dual Burnside process and established the general \(AB/BA\) factorization, stationary distribution, spectral correspondence, and conjugacy lumping; all of those general ingredients are explicitly credited. In a transitive action, its orbit/conjugacy quotient theorem already implies one-step stationarity on conjugacy classes. The distinct assertion here is the full **sharp total-variation profile for all doubly transitive actions with a singleton fixer**, the explicit comparative exponents for natural symmetric and affine families, and their resulting mixing-time separation. The general factorization alone does not state these group-dependent constants or sharp supremum; they require the two-orbit stabilizer calculation, exact maximizer and the two families' fixed-point enumerations. Nevertheless, the specialization is elementary from the existing general theory, so precedence by unrecognized published specializations remains a live risk.

## Limitations
This establishes no cutoff claim. Without an element fixing exactly one point, the fixed-start geometric decay remains exact but the universal sharp worst-start prefactor is only an upper bound. The comparison concerns these two explicitly specified permutation actions, not general naturality or efficiency across all group actions. The conjugacy-class instantaneous equilibrium is not claimed as original. Priority under alternative names for random walks generated by point stabilizers remains possible. Independent external validation has not been performed.

## References
1. I. Z. Feng, *The dual Burnside process*, arXiv:2510.25202, first submitted 2025-10-29; *Journal of Theoretical Probability* 39, article 78 (2026), doi:10.1007/s10959-026-01539-9. Full open-access research article at https://link.springer.com/article/10.1007/s10959-026-01539-9.
2. Standard finite-group tools used explicitly: orbit–stabilizer theorem, Burnside's orbit-counting lemma, and basic symmetric/affine permutation group actions.
