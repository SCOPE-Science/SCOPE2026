# Strict left-half-plane independence-root stability of double-star trees

## Finding
For any integers \(a,b\geq0\), form the double-star tree \(D_{a,b}\) by joining two vertices \(u,v\) and attaching \(a\) pendant leaves to \(u\) and \(b\) pendant leaves to \(v\). Its independence polynomial is
\[
I(D_{a,b};z)=(1+z)^{a+b}+z\bigl((1+z)^a+(1+z)^b\bigr).
\]
**Theorem.** For every such pair and every complex \(z\) with \(\operatorname{Re}z\geq0\), the displayed polynomial is nonzero. Thus every independence root of every nonempty tree of diameter at most three lies in the **open** left half-plane. The two-branching-center cases \(a,b\geq2\) extend beyond the spider family.

## Assumptions and scope
All graphs are finite, simple, undirected, with the convention that \(D_{0,0}=K_2\). An independent set is a vertex subset spanning no edge; \(I(G;z)=\sum_{S\text{ independent}}z^{|S|}\), including the empty set. A tree of diameter one, two or three is respectively an edge, a star, or a double star. The single-vertex tree has polynomial \(1+z\), which also has only strictly negative-real-part roots. No statement is made about trees of diameter greater than three.

## Proof
**Exact polynomial.** Partition independent sets according to whether they contain neither, exactly \(u\), or exactly \(v\). Both centers cannot be chosen. Choosing neither gives \((1+z)^{a+b}\); choosing \(u\) allows every leaf attached to \(v\), contributing \(z(1+z)^b\); choosing \(v\) gives \(z(1+z)^a\). This proves the identity with all coefficients and boundary cases.

By symmetry, assume \(0\leq a\leq b\). Fix an arbitrary \(z\in\mathbb C\) with \(x=\operatorname{Re}z\geq0\), and let \(r=|z|\), \(s=|1+z|\). We have
\[
s^2=1+2x+r^2,\qquad s>r,\qquad s\geq1,\qquad s^2-2r=(r-1)^2+2x\geq0.
\]
The inequalities are strict where stated, since \(s^2-r^2=1+2x>0\).

**Case \(a=0\).** The polynomial becomes \((1+z)^{b+1}+z\). As \(b+1\geq1\) and \(s\geq1\), its two summands have distinct moduli: \(s^{b+1}\geq s>r\). Hence their sum is nonzero.

**Case \(a=1\).** Since \(b\geq1\), factor the polynomial as
\[
I(D_{1,b};z)=(1+z)\bigl((1+2z)(1+z)^{b-1}+z\bigr).
\]
Here \(1+z\ne0\) and
\[
|1+2z|^2-|z|^2=1+4x+3r^2>0.
\]
Therefore \(|(1+2z)(1+z)^{b-1}|\geq|1+2z|>r\), so the second factor is nonzero.

**Case \(a\geq2\).** Suppose, for contradiction, that the polynomial vanishes. Since its constant term is one, \(z\ne0\), hence \(s>1\). Dividing its defining identity by \((1+z)^b\) gives
\[
(1+z)^a=-z\bigl(1+(1+z)^{a-b}\bigr).
\]
Taking moduli and applying the triangle inequality gives
\[
s^a\leq r(1+s^{a-b})\leq2r\leq s^2\leq s^a.
\]
If \(a<b\), the second inequality is strict because \(s>1\) and \(a-b<0\), a contradiction. If \(a=b>2\), the final inequality is strict because \(s>1\), again a contradiction. Finally, when \(a=b=2\), equality throughout forces \(2r=s^2\), i.e. \((r-1)^2+2x=0\), so \(z=i\) or \(z=-i\). The vanishing equation simplifies to \((1+z)^2+2z=0\), but its value at these two candidates is respectively \(4i\) and \(-4i\), contradiction.

Thus no zero lies in the closed right half-plane, establishing the claim for all nonnegative parameters. Every finite tree with at least two vertices and diameter at most three belongs to this family, while the singleton case is immediate. \(\square\)

## Verification
The accompanying dependency-free Python file `verify_double_stars.py` independently constructs each double-star graph, enumerates its vertex subsets, and compares its exact independence-polynomial coefficient tuple with the displayed formula for every \(0\leq a,b\leq8\) (81 profiles; 1,044,484 tested subsets). It additionally builds exact rational Routh arrays for every \(0\leq a,b\leq15\) (256 profiles) and checks positivity of their first-column entries. Both checks completed successfully; their exact output is embedded as `verification_output.txt`. The algebraic proof, not finite enumeration or the Routh tests, covers all parameters.

## Relationship to prior work
Brown and Cameron [1] proved stability for stars and graphs with independence number at most three and exhibited nonstable trees. Zhang and Tu [2] prove strict stability for spiders, a family with at most one branching vertex, but the double stars with \(a,b\geq2\) have two adjacent branching vertices and unbounded independence number. Hibi, Kara and Vien [3, Proposition 3.1] give a general formula for independence polynomials under leaf attachment, which includes the **displayed polynomial identity as a known special case**; their result concerns polynomial enumeration, symmetry, and evaluation at \(-1\), not its half-plane root location. Bencs [4, Proposition 3.4] proved real-rootedness for a specific uniformly two-whiskered path family; its two-spine-vertex member is \(D_{2,2}\). His proposition does not imply stability of general \(D_{a,b}\): for instance \(D_{2,3}\) has nonreal independence roots. The present assessed finding is the full, strict root-location theorem, not novelty of the polynomial expression or of any previously settled boundary family.

## Limitations
The result treats only finite diameter-at-most-three trees. It gives a strict zero-free half-plane but no uniform quantitative negative-real-part margin as \(a,b\) vary. Several special cases are established elsewhere, and an unindexed equivalent theorem under other graph terminology is a residual literature risk. Computational checks are finite corroboration rather than an infinite certificate; no external independent audit is claimed.

## References
[1] J. I. Brown and B. Cameron, *On the Stability of Independence Polynomials*, arXiv:1802.02478v1 (2018), https://arxiv.org/html/1802.02478v1.

[2] L. Zhang and J. Tu, *Stability of independence polynomials of spiders*, arXiv:2609.04694v1 (first posted 2026-09-04 UTC), https://arxiv.org/html/2609.04694v1.

[3] T. Hibi, S. Kara and D. Vien, *Independence Polynomials of Graphs*, arXiv:2603.16695v1 (2026), https://arxiv.org/html/2603.16695v1.

[4] F. Bencs, *On trees with real rooted independence polynomial*, arXiv:1703.05409v1 (2017), https://arxiv.org/html/1703.05409v1.
