# Exact scalar annulus for super-asymptotic expansivity on Banach spaces

## Finding

Let \(X\neq\{0\}\) be a complex Banach space and \(T\in\mathcal B(X)\). For a bounded operator \(A\) define its minimum modulus
\[
m(A)=\inf_{\|x\|=1}\|Ax\|.
\]
Write
\[
r(T)=\lim_{n\to\infty}\|T^n\|^{1/n},\qquad
\rho_-(T)=\lim_{n\to\infty}m(T^n)^{1/n}.
\]
The second limit exists and belongs to \([0,r(T)]\); if \(m(T)=0\), it is zero. The first is the usual spectral radius; the second is a lower growth radius, not necessarily the minimum absolute value in the spectrum for a non-surjective operator.

**Exact scalar classification.** For every \(c\in\mathbb C\), the operator \(cT\) is super-asymptotically expansive in the sense of [1, Definition 3.3] **if and only if**
\[
\boxed{|c|r(T)<1\quad\text{or}\quad |c|\rho_-(T)>1.}
\]
An equivalent intrinsic characterization is
\[
A\text{ super-asymptotically expansive}
\ \Longleftrightarrow\ 
\bigl(\exists k\ge1:\|A^k\|<1\bigr)
\ \text{or}\ 
\bigl(\exists k\ge1:m(A^k)>1\bigr).
\]
If \(0<\rho_-(T)\le r(T)\), the excluded scalar parameters form exactly the **closed annulus**
\[
\frac1{r(T)}\le|c|\le\frac1{\rho_-(T)}.
\]
Neither boundary circle is included in the allowed region. If \(\rho_-(T)=0<r(T)\), the forbidden set is \(\{|c|\ge1/r(T)\}\); if \(r(T)=0\), every finite scalar is allowed.

## Assumptions and scope

The space \(X\) is nonzero and complex and need not be separable, reflexive, a Hilbert space, finite-dimensional, or equipped with a basis. The operator \(T\) is bounded but need not be injective or surjective. No normality, spectral splitting, or hyperbolicity is assumed. By [1, Definition 3.3], \(A\) is super-asymptotically expansive if, for every \(\varepsilon,M>0\), some integer \(N\ge1\) has the property that every unit vector \(x\) satisfies either \(\|A^n x\|<\varepsilon\) for all \(n\ge N\), or \(\|A^n x\|>M\) for all \(n\ge N\). The alternative may depend on \(x\); the same \(N\) must serve every unit vector.

## Proof

**Step 1: the uniform alternative collapses to one global branch.** The unit sphere \(S_X=\{x:\|x\|=1\}\) of a nonzero complex normed space is path-connected. Indeed, noncollinear unit vectors can be joined by normalized straight segments; unit vectors on the same complex line can be joined by a continuous complex-phase rotation. Choose \(\varepsilon=1/2\), \(M=2\) in the defining condition. At the resulting common time \(N\), every \(x\in S_X\) satisfies \(\|A^Nx\|<1/2\) or \(\|A^Nx\|>2\). The continuous image \(\{\|A^Nx\|:x\in S_X\}\) is connected and lies in the union of two disjoint intervals \([0,1/2)\cup(2,\infty)\). Therefore it lies entirely in one interval. Hence either \(\|A^N\|\le1/2<1\) or \(m(A^N)\ge2>1\).

**Step 2: each global branch suffices.** If \(\|A^k\|=a<1\), write \(n=kq+j\), \(0\le j<k\). Then \(\|A^n\|\le a^q\max_{0\le j<k}\|A^j\|\to0\). The small alternative consequently holds uniformly for all unit vectors. If \(m(A^k)=b>1\), then \(m(A)>0\) (otherwise \(m(A^k)\le\|A\|^{k-1}m(A)=0\)). The inequalities \(m(BC)\ge m(B)m(C)\) and \(n=kq+j\) yield
\[
m(A^n)\ge b^q\min_{0\le j<k}m(A^j)\longrightarrow\infty.
\]
Thus the large alternative holds uniformly. This proves the intrinsic characterization with all quantifiers and both strict thresholds.

**Step 3: growth rates give the scalar phase.** Submultiplicativity of \(\|T^n\|\) and the spectral-radius formula give \(r(T)=\inf_{n\ge1}\|T^n\|^{1/n}\). If \(m(T)>0\), supermultiplicativity of \(m(T^n)\) and the superadditive limit lemma applied to logarithms give \(\rho_-(T)=\sup_{n\ge1}m(T^n)^{1/n}\); if \(m(T)=0\), then \(m(T^n)=0\) for every \(n\ge1\) and the same equivalence of thresholds holds. For every scalar \(c\),
\[
\|(cT)^n\|=|c|^n\|T^n\|,\qquad
m((cT)^n)=|c|^n m(T^n).
\]
Hence \(\exists k:\|(cT)^k\|<1\) is equivalent to \(|c|r(T)<1\); likewise \(\exists k:m((cT)^k)>1\) is equivalent to \(|c|\rho_-(T)>1\). In particular, equality to either threshold cannot qualify. Since \(m(T^n)\le\|T^n\|\), the lower radius never exceeds the upper radius, completing the annulus description.

## Verification

The proof is an infinite-dimensional argument using a connected unit sphere, a single time extracted from the exact uniform quantifiers, and two multiplicative inequalities; it has no computational certificate dependency. Two explicit checks illustrate distinct portions of the theorem.

For \(T=\operatorname{diag}(1/2,2)\) on Euclidean \(\mathbb C^2\), one has \(r(T)=2\) and \(\rho_-(T)=1/2\). Thus \(cT\) qualifies precisely for \(|c|<1/2\) or \(|c|>2\), with the entire intermediate closed annulus excluded, even though most such intermediate scalars give hyperbolic operators.

For the unilateral forward isometry \(S\) on \(\ell^2(\mathbb N)\), let \(T=2S\). Every power satisfies \(\|T^n\|=m(T^n)=2^n\), so both radii equal \(2\). Here \(cT\) is super-asymptotically expansive for **every** \(|c|\ne1/2\): uniform contraction below the circle and uniform expansion above it. In particular, \(2S\) itself qualifies although \(\sigma(2S)=\{z:|z|\le2\}\) intersects the unit circle. At \(|c|=1/2\), \(cT\) is isometric and fails the definition.

## Relationship to prior work

Bag, Mandal, and Das [1] introduce the exact notion in Definition 3.3 and state in Theorem 4.5 and Proposition 5.3 criteria based on hyperbolicity and avoidance of a unit-circle spectral set. The two criteria do not imply the present classification: a hyperbolic operator with both stable and unstable components violates the definition, while \(2S\) is super-asymptotically expansive without being hyperbolic. Our statement provides the full scalar characterization for every bounded operator rather than the proposed spectral-gap classification. Its proof exploits path-connectedness and the **minimum modulus of powers**, neither of which appears in their scalar proposition.

Bernardes Jr., Cirilo, Darji, Messaoudi, and Pujals [2, Section 2, Proposition 5(b)] characterize uniformly positive expansivity by uniform divergence of iterates. That classical expansion branch agrees with one side of our dichotomy, but [2] does not formulate the newly defined super-asymptotic alternative or the two-radius scalar annulus; uniform expansivity in [2] also permits separate forward/backward behavior and is not the present forward-time definition.

## Limitations

The theorem concerns exactly Definition 3.3 of [1], not the different notions called asymptotic expansivity, strong asymptotic expansivity, uniform expansivity, or shadowing. It does not classify those other notions. The lower growth radius is a minimum-modulus growth limit, not the inner boundary of the full spectrum for nonsurjective operators; replacing it by the inner spectral modulus would make the theorem false. Novelty comparisons remain limited by the coverage of the inspected and indexed mathematical literature, and no independent audit has been performed.

## References

[1] P. Bag, P. N. Mandal, P. K. Das, *Asymptotic Expansive and Hyperbolic Linear Operators*, arXiv:2610.01196v1 (first publicly posted 2026-10-01), Definition 3.3, Theorem 4.5, Example 4.1, Theorem 4.13 and Proposition 5.3. https://arxiv.org/abs/2610.01196

[2] N. C. Bernardes Jr., P. R. Cirilo, U. B. Darji, A. Messaoudi, E. R. Pujals, *Expansivity and Shadowing in Linear Dynamics*, arXiv:1612.02921v1 (2016), §2, especially Definitions 1–2 and Proposition 5; J. Math. Anal. Appl. 461 (2018), 796–816. https://arxiv.org/abs/1612.02921
