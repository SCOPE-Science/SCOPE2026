# A circle–sphere bouquet theorem for a family of rational-function fibers

## Finding
For each pair of integers \(n\ge3\), \(m\ge2\), let \(p\in\mathbb C[x]\) be a degree-\(m\) polynomial with \(p(0)=0\) and \(p'(0)\ne0\). Put \(q(y_1,\ldots,y_{n-1})=\sum_{j=1}^{n-1}y_j^2\) and define the regular map on the indicated principal open set
\[
 f_p:\mathbb C^*\times\mathbb C^{n-1}\longrightarrow\mathbb C,
 \qquad (x,y)\longmapsto p(x)+\frac{q(y)}{x}.
\]
For every \(c\in\mathbb C\setminus\bigl(\{0\}\cup\{p(z):p'(z)=0\}\bigr)\), its fiber \(F_{p,c}=f_p^{-1}(c)\) is smooth, connected, and has the integral homotopy type
\[
 \boxed{F_{p,c}\simeq S^1\vee\bigvee_{j=1}^{m}S^{n-1}.}
\]
In particular \(\pi_1(F_{p,c})\cong\mathbb Z\), \(H_0(F_{p,c};\mathbb Z)=H_1(F_{p,c};\mathbb Z)=\mathbb Z\), \(H_{n-1}(F_{p,c};\mathbb Z)=\mathbb Z^m\), and all other reduced integral homology groups vanish. These are homotopy statements, not merely rational cohomology calculations.

## Assumptions and scope
The topology is the ordinary classical topology of the complex algebraic fiber. The indicated set of \(c\)-values is nonempty and Zariski open; it excludes both \(c=0\) and all critical values of \(p\). No genericity assumptions on the locations of distinct roots of \(p\) are needed beyond \(p'(0)\ne0\). Denote \(k=n-1\ge2\) and \(h_c(x)=x(c-p(x))\). The nonzero zeros of \(h_c\) are exactly the \(m\) simple roots of \(p(x)=c\), because \(c\ne0\).

## Proof
**1. The total fiber is smooth and has the required quadric projection.** The defining equation is \(q(y)=h_c(x)\), with \(x\in\mathbb C^*\). Its gradient in the \(y\)-variables vanishes only at \(y=0\). At a point with \(y=0\), the equation requires \(h_c(x)=0\), and the derivative in \(x\) is \(-xp'(x)\ne0\), since \(x\ne0\) and \(c\) is not a critical value. Thus \(F_{p,c}\) is nonsingular of complex dimension \(n-1\).

**2. Regular quadric fibers are spheres up to homotopy.** Projection \(\rho:F_{p,c}\to\mathbb C^*\), \((x,y)\mapsto x\), has smooth fibers \(q^{-1}(h_c(x))\) wherever \(h_c(x)\ne0\). Choosing a continuous square root of the nonvanishing function \(h_c\) on a simply connected base patch gives a homeomorphism of the restriction of \(\rho\) with the product of that patch and \(A=q^{-1}(1)\). If \(y=a+ib\in A\), with \(a,b\in\mathbb R^k\), then \(a\cdot b=0\) and \(|a|^2-|b|^2=1\). The formula
\[
 y_t=\sqrt{1+t^2|b|^2}\,\frac{a}{|a|}+itb,
 \quad 0\le t\le1,
\]
gives a deformation retraction of \(A\) to the real unit sphere \(S^{k-1}=S^{n-2}\).

**3. The simple-zero neighborhoods contribute exactly cones.** At a root \(r\) of \(p(x)=c\), the derivative \(h_c'(r)=-rp'(r)\ne0\). Hence \(u=h_c(x)\) is a complex coordinate on a sufficiently small disk around \(r\). Over this disk, \(\rho\) is topologically the standard quadratic family \(q(y)=u\). The preimage of a sufficiently small closed \(u\)-disk is identified with \(\{y:|q(y)|\le\varepsilon\}\), which contracts by \(y\mapsto sy\), \(0\le s\le1\). The preimage of its radial interval \([0,\varepsilon]\) contracts in the same way, and its regular endpoint fiber is \(A\). Thus this piece, glued to the regular part along its endpoint fiber, has the homotopy-pushout effect of attaching \(CA\), the cone on \(A\).

**4. Global reduction to one mapping torus and \(m\) cones.** In the punctured \(x\)-plane choose an embedded graph consisting of a single circle surrounding the omitted origin and \(m\) disjoint narrow stems from that circle to the roots of \(p(x)=c\). This graph is a spine of \(\mathbb C^*\). To justify using this spine for the total space, cover the base by regular simply connected patches, regular collars of the stems, and the small disks in Step 3. On regular patches the map is an explicit product bundle by square-root trivialization; on the singular disks and their radial subintervals the total spaces are contractible by Step 3. Pruning complementary base disks in this cover changes neither the local fiber homotopy types nor their intersection maps. Gluing the resulting product and cone pieces along their regular fiber intersections (or using their mapping-cylinder homotopy pushouts) yields
\[
 F_{p,c}\simeq M_{\varphi}(A)\ \cup_{A_1}CA\ \cup_{A_2}CA\ \cdots\ \cup_{A_m}CA.
\]
Here \(M_{\varphi}(A)\) is the mapping torus of the square-root monodromy of \(A\) around the origin; transport along each stem identifies \(A_j\) up to homotopy with a chosen fiber \(A\) of the mapping torus. The formula uses no properness assertion for \(\rho\); the product structure and contractions are explicit.

**5. Homotopy pushout calculation.** Attach the first cone. Since a regular fiber of the mapping torus is a cofibration up to mapping cylinder, its homotopy quotient is
\[
 M_{\varphi}(A)/A\cong (A\times[0,1])/(A\times\{0,1\}\text{ collapsed to one point}).
\]
Because \(A\simeq S^{n-2}\) is connected, the quotient is \(S^1\vee\Sigma A\simeq S^1\vee S^{n-1}\); the monodromy disappears because both ends were collapsed. The regular fiber inclusions for the remaining \(m-1\) cones are nullhomotopic after the first cone. Each further attachment therefore wedges on another suspension \(\Sigma A\simeq S^{n-1}\). The displayed homotopy equivalence follows, with all integral homotopy and homology consequences claimed above.

## Verification
The assumptions yield exactly \(m\) nonzero simple zeros of \(h_c\), with \(h_c'(r)=-rp'(r)\). The quadratic regular fiber retracts by the displayed explicit formula. The local disk is star-shaped under \(y\mapsto sy\), so each singular-fiber attachment is contractible and meets the regular part along a quadric Milnor fiber. The mapping-torus quotient and subsequent nullhomotopic attachments establish the full homotopy type for arbitrary \(n,m\), without a finite-sample extrapolation. As an independent consistency check, additivity of Euler characteristic and the local fiber description give \(\chi(F_{p,c})=m(-1)^{n-1}\), in agreement with the bouquet: \(\chi(\mathbb C^*\setminus\{r_1,\dots,r_m\})=-m\), so \(\chi(F)=(-m)\bigl(1+(-1)^{n-2}\bigr)+m=m(-1)^{n-1}\). This consistency check does not substitute for the homotopy proof.

## Relationship to prior work
Takeuchi (arXiv:2610.20025v1, Theorem 3.3 and Conjectures 3.7/3.9) proves a cohomological concentration statement for suitable tame rational-function fibers and proposes a circle-and-spheres **homotopy** type. The present theorem verifies that stronger homotopy conclusion and determines the exact sphere count for an explicit infinite family, using the projection of the fiber to the punctured coordinate line. Neither Takeuchi's cohomology statement nor a conjecture by itself implies this homotopy equivalence. The classical theory of affine quadratic Milnor fibers supplies the local ingredient. Dubouloz's Danielewski–Fieseler work treats additive actions, affine-line fibrations, rooted-tree classification and embeddings; its stated results do not yield this punctured-base, higher-dimensional homotopy type. In complex dimension two, related Danielewski presentations present a genuine historical-priority risk; no global novelty claim is made against unexamined results on such affine surfaces or generalized quadric fibrations.

## Limitations
This is an explicit family result, not a proof of Takeuchi's general conjectures. The level must avoid the listed finite set of parameters; no assertion concerns its exceptional fibers, arbitrary rational numerators or denominators, other quadratic ranks, or the existence of a canonical choice of bouquet equivalence. The argument assumes complex topology and \(n\ge3\). Classical Lefschetz-fibration and Danielewski literature may contain more general implicit formulations; priority beyond the inspected comparisons remains uncertain.

## References
1. Kiyoshi Takeuchi, *On the Topology of Fibers of Rational Functions*, arXiv:2610.20025v1 (2026), especially Theorem 3.3 and Conjectures 3.7, 3.9. https://arxiv.org/html/2610.20025v1
2. Adrien Dubouloz, *Danielewski-Fieseler surfaces*, arXiv:math/0401225 (2004). https://arxiv.org/abs/math/0401225
3. S. A. Broughton, *Milnor numbers and the topology of polynomial hypersurfaces*, Invent. Math. 92 (1988), 217–241; referenced for background only.
