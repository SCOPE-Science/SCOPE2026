# Positive-cone extremizers for a four-point Lipschitz-free \(p\)-space embedding

## Finding
For each \(0<p<1\), fix a four-point tree with equal leaf arms and a variable positive stem length. Among **all nonnegative leaf coefficient vectors** and all stem lengths, the exact largest ratio of the canonical Lipschitz-free \(p\)-space norms is
\[
\Gamma_p=\max\left\{1,\left(\frac{2(1+h_p)^p}{2^p h_p^p+2}\right)^{1/p}\right\},\qquad
h_p=\left(\frac{2^p}{2-2^p}\right)^{1/p}-1.
\]
Whenever \(\Gamma_p>1\), every maximizer has equal strictly positive leaf coefficients and the unique stem length \(h_p\), up to scaling of the coefficients. The exact gain criterion is \(2(1+h_p)^p>2^ph_p^p+2\). At \(p=2/3\), the ratio is approximately \(1.027846\); the statement neither asserts nor requires uniqueness of a threshold in \(p\).

## Assumptions and scope
Let \(0<p<1\). Give \(M_h=\{0,z,x,y\}\) the ordinary path metric with positive edge lengths \(d(0,z)=h\), \(d(z,x)=d(z,y)=1\). The pointed subspace is \(N_h=\{0,x,y\}\). The Dirac maps \(\delta_x,\delta_y\) use base point \(0\). The norms are those of the real Lipschitz-free quasi-Banach \(p\)-spaces, with their canonical convention that the \(p\)-th power is computed by a minimum over spanning-tree molecule decompositions. For \(u,v\geq0\), not both zero, define \(R_p(h;u,v)=\|u\delta_x+v\delta_y\|_{\mathcal F_p(N_h)}/\|u\delta_x+v\delta_y\|_{\mathcal F_p(M_h)}\). The theorem concerns \(\sup R_p\) on **this positive cone and equal-arm family only**, not the full inverse operator norm.

## Proof
Write \(c=(h+1)^p\), \(q=2^p\), and \(S=u^p+v^p\). The three rooted trees on \(N_h\) have edge-cost \(p\)-powers
\[
\|u\delta_x+v\delta_y\|_{\mathcal F_p(N_h)}^p
=\min\left\{cS,\ c(u+v)^p+qu^p,\ c(u+v)^p+qv^p\right\}.
\]
The spanning-tree formula (Cúth--Raunig, Theorem 2.2) and its one-Steiner-point reduction (their Proposition 3.5) give
\[
\|u\delta_x+v\delta_y\|_{\mathcal F_p(M_h)}^p
=\min\left\{\|u\delta_x+v\delta_y\|_{\mathcal F_p(N_h)}^p,\ h^p(u+v)^p+S\right\}.
\]
Indeed, a potentially improving tree must have \(z\) as the parent of both \(x\) and \(y\); trees in which \(z\) has at most one descendant reduce to a tree entirely on \(N_h\). Accordingly,
\[
R_p(h;u,v)^p=\max\left\{1,\frac{\min\{cS,c(u+v)^p+q\min(u^p,v^p)\}}{h^p(u+v)^p+S}\right\}.
\]
Normalize \(u+v=1\), let \(t=\min(u,v)\in[0,1/2]\), and put \(S(t)=t^p+(1-t)^p\), \(D(t)=h^p+S(t)\). Both branches \(cS(t)/D(t)\) and \((c+qt^p)/D(t)\) are strictly increasing for \(0<t<1/2\). For the first, \(S'(t)>0\) and \(h>0\). For the second, \(c\leq h^p+1\leq qh^p+q(1-t)^p\), hence \(c+qt^p\leq qD(t)\), so
\[
\frac{d}{dt}\frac{c+qt^p}{D(t)}
=\frac{qp t^{p-1}D(t)-(c+qt^p)p[t^{p-1}-(1-t)^{p-1}]}{D(t)^2}
\geq \frac{qp(1-t)^{p-1}}{D(t)}>0.
\]
Therefore the two-branch minimum, and hence the ratio whenever above one, is maximized uniquely at \(u=v\).

Set \(u=v=1\). Then
\[
R_p(h;1,1)^p=\max\left\{1,\frac{\min\{2(h+1)^p,q((h+1)^p+1)\}}{qh^p+2}\right\}.
\]
The two numerator branches cross once when \((h+1)^p=q/(2-q)\), namely \(h=h_p\). Moreover \(h_p>1/2\): it is enough to check \(2^p+(4/3)^p>2\), which holds for \(p>0\). For \(0<h\leq h_p\), the relevant nonconstant branch is \(2(h+1)^p/(qh^p+2)\), with derivative sign equal to the sign of \(2-qh^{p-1}\). It decreases until \(h=1/2\) and then increases, so its maximum on this interval is at an endpoint; the limit at zero is one. For \(h\geq h_p\), the relevant branch minus one is
\[
\frac{q[(h+1)^p-h^p]-(2-q)}{qh^p+2}.
\]
The numerator decreases strictly and the denominator increases strictly with \(h\), so wherever this difference is positive it strictly decreases. Thus no \(h>h_p\) can exceed the larger of one and the value at \(h_p\). These observations yield the formula and, in the gain regime, uniqueness of \(h_p\), \(u=v>0\). This completes the proof.

## Verification
The proof is analytic for all real \(p\) with \(0<p<1\); it uses no finite enumeration as a substitute for an infinite argument. Substituting \(p=1/2\) gives a strict subunit nontrivial branch and hence \(\Gamma_p=1\); substituting \(p=2/3\) gives \(\Gamma_p\approx1.027846\), agreeing with the parameter and lower bound of the source's Proposition 3.24. The derived formula agrees algebraically with its equal-coefficient lower-bound expression when \(q=1\).

## Relationship to prior work
Cúth and Raunig give the spanning-tree norm algorithm (Theorem 2.2), reduction to Steiner trees (Propositions 3.5--3.6), and an equal-coefficient, particular-stem **lower bound** for three-point embeddings (Proposition 3.24). Their bound exactly equals our maximizing value **within the family studied here**. The new assertion is a quantified sharp optimality and uniqueness classification across *all nonnegative coefficients and all positive stem lengths within that family*, which does not follow merely from exhibiting their witness. Their open Question 3 is not resolved; its resolution may depend on other tree shapes or signed vectors. A separately indexed result on universal three-point \(p\)-metric inclusion constants treats the broader \(p\)-metric supercategory, not the ordinary-metric, positive-cone restriction proved here.

## Limitations
This does not establish a globally sharp \(\mathfrak{aa}_p^1(2)\) bound or whether the full canonical embedding is isometric. Unequal leaf-arm lengths, signed coefficients, larger superspaces, and general three-point metrics are outside the theorem. No unique transition exponent is claimed. Published-literature coverage is assessed from the original full arXiv text and targeted searches; it remains possible that an independent source contains this restricted optimization.

## References
1. M. Cúth and T. Raunig, *Canonical embedding of Lipschitz-free p-spaces*, arXiv:2311.02920v1 (first public version 2023-11-06), Theorem 2.2, Propositions 3.5 and 3.24, Questions 2--3. https://arxiv.org/html/2311.02920v1
2. published-finding corpus record `2026/10/11/SCOPE-exact-three-point-lipschitz-free-p-inclusion-constant--2bd77d9d9d70`, covering the universal \(p\)-metric three-point constant (different ambient metric class).
