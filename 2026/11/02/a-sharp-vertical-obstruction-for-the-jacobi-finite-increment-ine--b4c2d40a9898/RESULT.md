# A sharp vertical obstruction for the Jacobi finite-increment inequality

## Finding
Write \(P_n^{(\alpha,\beta)}\) for the standard Jacobi polynomial with \(P_n^{(\alpha,\beta)}(1)=\Gamma(n+\alpha+1)/[\Gamma(\alpha+1)\Gamma(n+1)]\). Fix \(\alpha,\beta>-1\), and define the finite-increment defect
\[
E_n^{\alpha,\beta}(x)=P_n^{(\alpha,\beta)}(1)-P_n^{(\alpha,\beta)}(x)-(1-x)(P_n^{(\alpha,\beta)})'(x),\qquad 0\le x\le1.
\]
Put \(\delta=\pi(\beta-\alpha)/4\), \(c_{\alpha,\beta}=2^{(\alpha+\beta+1)/2}/\sqrt\pi\), and \(m(\delta)=\max\{|\sin\delta|,|\cos\delta|\}\). The exact signed lower asymptotic at the origin is
\[
\boxed{\liminf_{n\to\infty}\frac{E_n^{\alpha,\beta}(0)}{\sqrt n}=-c_{\alpha,\beta}m(\delta)<0}\qquad(-1<\alpha<\tfrac12),
\]
and on the boundary \(\alpha=\tfrac12\) it is
\[
\boxed{\liminf_{n\to\infty}\frac{E_n^{1/2,\beta}(0)}{\sqrt n}=\frac{2}{\sqrt\pi}\Bigl[1-2^{(\beta-1/2)/2}m\bigl(\pi(\beta-1/2)/4\bigr)\Bigr].}
\]
Consequently, if the finite-increment inequality \(E_n^{\alpha,\beta}(x)\ge0\) holds for **every** integer \(n\ge3\) and **every** \(x\in[0,1]\), then necessarily \(\alpha\ge\tfrac12\); moreover on the boundary \(\alpha=\tfrac12\) one must have
\[
2^{(\beta-1/2)/2}\max\left\{\left|\sin\frac{\pi(\beta-1/2)}4\right|,\left|\cos\frac{\pi(\beta-1/2)}4\right|\right\}\le1.
\]
In particular every \(\beta\ge\tfrac52\) is excluded when \(\alpha=\tfrac12\). Combined with the known sufficient result for \(\alpha=\beta\ge\tfrac12\), this gives the **complete sharp ultraspherical classification**:
\[
\boxed{E_n^{\alpha,\alpha}(x)\ge0\ \text{for all }n\ge3,\ x\in[0,1]\quad\Longleftrightarrow\quad\alpha\ge\tfrac12.}
\]
The boundary \(\alpha=\tfrac12\) is attained, so the two-dimensional necessary lower bound is sharp. The theorem does not classify the entire admissible region above this boundary.

## Assumptions and scope
The Jacobi parameters \(\alpha,\beta\) are fixed real numbers greater than \(-1\); the degree \(n\) tends through positive integers. Jacobi polynomials have the conventional positive endpoint normalization specified above, without a degree-dependent rescaling. The derivatives are with respect to \(x\); no normalization by \(P_n(1)\) is made in the defect. The inequalities concern the full interval \([0,1]\) and **all** degrees, not a single chosen degree. The origin is an allowed test point. The published sufficient theorem is explicitly distinguished from the new necessary asymptotic.

## Proof
**1. An exact origin reduction.** The standard Jacobi differentiation identity gives, for each integer \(n\ge1\),
\[
(P_n^{(\alpha,\beta)})'(0)=\frac{n+\alpha+\beta+1}{2}P_{n-1}^{(\alpha+1,\beta+1)}(0).
\]
The endpoint value is exactly \(\Gamma(n+\alpha+1)/[\Gamma(\alpha+1)\Gamma(n+1)]\), so by the gamma-ratio formula it equals \(n^\alpha/\Gamma(\alpha+1)(1+O_{\alpha}(n^{-1}))\).

**2. The oscillatory interior asymptotics.** The classical Darboux formula for Jacobi polynomials (DLMF, §18.15(i), formula 18.15.4_5), evaluated at \(x=\cos(\pi/2)=0\), yields for all fixed parameters greater than \(-1\):
\[
P_n^{(\alpha,\beta)}(0)=\frac{2^{(\alpha+\beta+1)/2}}{\sqrt{\pi n}}\cos\left(\frac{n\pi}{2}+\delta\right)+O_{\alpha,\beta}(n^{-3/2}).
\]
Apply the same formula to \(P_{n-1}^{(\alpha+1,\beta+1)}\), whose angular phase has the same \(\delta\). The exact differentiation identity then implies
\[
(P_n^{(\alpha,\beta)})'(0)=c_{\alpha,\beta}\sqrt n\sin\left(\frac{n\pi}{2}+\delta\right)+O_{\alpha,\beta}(n^{-1/2}).
\]
The phase identity is \(\cos((n-1)\pi/2+\delta)=\sin(n\pi/2+\delta)\). The asymptotic error is controlled at the fixed interior point; the proof does not differentiate an unproved uniform remainder.

**3. Quantitative degree-subsequence obstruction.** Substituting in the exact definition gives
\[
\frac{E_n^{\alpha,\beta}(0)}{\sqrt n}=\frac{n^{\alpha-1/2}}{\Gamma(\alpha+1)}(1+O_\alpha(n^{-1}))-c_{\alpha,\beta}\sin\left(\frac{n\pi}{2}+\delta\right)+O_{\alpha,\beta}(n^{-1}).
\]
The possible limiting sine values along residue classes \(n\bmod4\) are precisely \(\sin\delta,\cos\delta,-\sin\delta,-\cos\delta\). Therefore their maximum is \(m(\delta)\ge1/\sqrt2>0\). When \(\alpha<1/2\), the gamma ratio term vanishes and the displayed liminf equals \(-c_{\alpha,\beta}m(\delta)\). In fact a fixed residue class realizes that negative limit; hence every such parameter pair has infinitely many degrees for which the inequality fails already at \(x=0\). This proves the universal necessary vertical boundary.

**4. The critical boundary and sharpness.** At \(\alpha=1/2\), the gamma ratio term tends to \(1/\Gamma(3/2)=2/\sqrt\pi\), proving the second displayed liminf. If the right side is negative, a fixed residue class violates the proposed all-degree inequality for every sufficiently large degree in that class. Rearranging its nonnegativity yields exactly the explicit phase-dependent necessary condition. For \(\beta\ge5/2\), the left-hand side of that condition is at least \(2^{(\beta-1/2)/2}/\sqrt2\ge\sqrt2>1\), so such boundary parameters fail. Finally, Nikolov's 2026 Theorem 1 proves the inequality for \(\alpha\ge\beta\ge1/2\), including every \(\alpha=\beta\ge1/2\). The necessity established in Step 3 gives the converse for the ultraspherical line. Thus both the sharp necessary vertical boundary and the exact diagonal classification follow, with no claim of complete classification off the diagonal.

## Verification
Independent finite checks of the *new algebra*, rather than the infinite theorem, are provided in `CHECK.py`. This checker verifies the Jacobi differentiation identity numerically across multiple parameters and degrees, compares the calculated derivative with its signed Darboux leading term along four residue classes, verifies the gamma endpoint formula, and checks failures for parameter pairs below the boundary. It does **not** infer the liminf from finite tests. The proof in Steps 1–4 supplies the infinite quantifiers through the classical Darboux remainder and the fixed residue-class limits.

## Relationship to prior work
Geno Nikolov, *An inequality for Jacobi polynomials: a complement to Finite Increment Theorem*, arXiv:2606.25468v1 (first public 24 June 2026), establishes the inequality on the sufficient regions \(\alpha\ge\beta\ge1/2\) and \(\alpha\ge1/2,\beta=-1/2\). Its Remark 1 expressly poses the determination of the full region of parameter pairs as a challenging open task. Its complete available text contains no universal necessary bound \(\alpha\ge1/2\), no residue-class liminf obstruction, and no global sharp diagonal if-and-only-if. These facts are not implied by a sufficient theorem alone. The DLMF classical Jacobi Darboux formula and standard gamma asymptotics are explicitly used as prior mathematical inputs: the contribution is their application to establish an exact four-phase obstruction for the newly posed all-degree inequality. Separate searches of related Jacobi parameter-bound and extrema results returned problems concerning different inequalities or zeros, not a logically covering theorem for this finite-increment defect.

## Limitations
Only the necessary half-plane and an explicit boundary restriction are proved for the general two-parameter domain; sufficiency outside the published sectors is not asserted. Along the diagonal the classification is complete by combining the present necessity with Nikolov's published sufficiency. The boundary necessary condition is not asserted sufficient. The proof uses fixed real Jacobi parameters and does not provide uniform estimates when the parameters vary with degree. A classical asymptotic formula is an indispensable established ingredient; an unindexed historical application of the same formula to this particular all-degree inequality remains an originality risk. Independent external verification has not been performed.

## References
1. G. Nikolov, *An inequality for Jacobi polynomials: a complement to Finite Increment Theorem*, arXiv:2606.25468v1, first public 2026-06-24, https://arxiv.org/abs/2606.25468. Theorem 1 and Remark 1 were inspected in the complete accessible research text.
2. NIST Digital Library of Mathematical Functions, §18.15(i), especially the Jacobi Darboux formula 18.15.4_5, https://dlmf.nist.gov/18.15. The formula and fixed-parameter remainder are classical.
3. G. Szegő, *Orthogonal Polynomials*, American Mathematical Society Colloquium Publications 23, fourth edition (1975), Chapter VIII (classical fixed-angle Jacobi asymptotics).
