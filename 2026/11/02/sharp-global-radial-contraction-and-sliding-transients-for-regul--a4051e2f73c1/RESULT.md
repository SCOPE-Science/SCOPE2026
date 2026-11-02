# Sharp global radial contraction and sliding transients for regular-polygon Filippov oscillators

## Finding
Fix an integer \(N\geq3\), \(\omega>0\), and \(\lambda>0\). Define the piecewise-affine planar oscillator and its Filippov boundary completion precisely below. Let \(C\) be the regular \(N\)-gon with unit-circumradius vertices. For every complete Filippov solution starting at a nonzero point, the polygonal gauge \(\rho\) obeys the **uniform sharp contraction law**
\[
 |\rho(x(t))-1|\leq e^{-\lambda\sin^2(2\pi/N)t}|\rho(x(0))-1|\qquad(t\geq0).
\]
The coefficient \(\lambda\sin^2(2\pi/N)\) cannot be increased while retaining prefactor one uniformly over initial states and Filippov solutions. Consequently \(\operatorname{dist}(x(t),C)\to0\) exponentially, no nonzero trajectory reaches the origin, and \(C\) is the sole nonconstant periodic trajectory of this inclusion outside the origin. Its traversal period is \(N/\omega\); the existence and period of this prescribed polygonal orbit are known from the source construction and are included only to state the global result completely.

There is an explicitly solvable regime of **attracting sliding** on every vertex ray. Write \(a=1-\cos(2\pi/N)\), \(b=\sin(2\pi/N)\). From an initial state \(x(0)=(1+z_0)p_j\), where \(z_0>\omega/(\lambda a)\), every forward Filippov trajectory initially slides on the vertex ray until \(z=\omega/(\lambda a)\); on this interval
\[
\dot z=-\lambda b^2z-\frac{\omega^2}{\lambda z},\qquad
 t_*=\frac{1}{2\lambda b^2}\log\left(\frac{z_0^2+\omega^2/(\lambda^2b^2)}{\omega^2/(\lambda^2a^2)+\omega^2/(\lambda^2b^2)}\right).
\]
In particular, large-radius sliding has a slower instantaneous relative radial dissipation rate than the interior sector flow; this mechanism sets the **sharp** global rate.

## Assumptions and scope
Index vertices cyclically as \(p_j=(\cos(2\pi j/N),\sin(2\pi j/N))\), with \(j=0,\ldots,N-1\). Put \(d_j=p_{j+1}-p_j\) and \(n_j=(d_{j,2},-d_{j,1})\). Then \(|d_j|^2=|n_j|^2=2a\), and \(n_j\cdot p_j=n_j\cdot p_{j+1}=b>0\). Let \(D_j=\{\alpha p_j+\beta p_{j+1}:\alpha,\beta\geq0\}\). In the interior of \(D_j\), prescribe
\[
 \dot x=F_j(x):=\omega d_j-\lambda(n_j\cdot x-b)n_j.
\]
This is the \(\mu_j=0\), common-\(\lambda_j\), common-\(\omega_j\) specialization of the affine coefficients (9) of Kai [1]. **The boundary rule used here differs from the source's transversal hybrid switching convention.** On each ray common to adjacent sectors, take the closed convex hull of the two limiting vectors (Filippov inclusion); no other switching or reset rule is imposed. At the origin take the full convex hull of all limiting values, but the theorem assumes \(x(0)\ne0\). A solution means an absolutely continuous Filippov solution satisfying the inclusion almost everywhere. The polygon gauge, defined for all \(x\), is
\[
\rho(x)=\frac1b\max_j n_j\cdot x.
\]
For \(x\ne0\), its value is positive, and \(\{\rho=1\}=C\). On the interior of \(D_j\), \(\rho(x)=n_j\cdot x/b\).

## Proof
**1. Sectorwise radial decay.** The normal and tangent are perpendicular, so for a solution in the interior of \(D_j\),
\[
 \dot\rho=\frac{n_j\cdot F_j(x)}{b}
 =-\lambda|n_j|^2(\rho-1)
 =-2\lambda a(\rho-1).
\]
Because \(a^2+b^2=2a\), we have \(2a\geq b^2\). Consequently \(\frac{d}{dt}|\rho-1|\leq-\lambda b^2|\rho-1|\) at interior times.

**2. Vertex-ray dynamics and all possible sliding solutions.** Rotational symmetry reduces the common ray at a vertex to \(x=(r,0)\), with the vertex at \((1,0)\). Put \(z=r-1\). The two limiting fields, indexed by previous and next sectors, are exactly
\[
 F^-(r,0)=(\omega a-\lambda b^2z,\ \omega b+\lambda ab z),\qquad
 F^+(r,0)=(-\omega a-\lambda b^2z,\ \omega b-\lambda ab z).
\]
If a Filippov solution stays on this ray over a set of times with positive measure, then its transverse velocity is zero almost everywhere on that set. Writing the convex combination \(qF^-+(1-q)F^+\), this requires
\[
 q=\frac12\left(1-\frac{\omega}{\lambda az}\right),\qquad 0\leq q\leq1,
\]
which is possible only when \(|z|\geq\omega/(\lambda a)\). Substitution into the radial component gives
\[
 \dot z=-\lambda b^2z-\frac{\omega^2}{\lambda z}.
\]
For \(z>0\) this is negative; for \(z<0\) it is positive. At tangencies with only isolated ray crossings, the ray times have measure zero and do not affect the differential inequality. More formally, because each ray is a fixed linear level set, the derivative of the transverse coordinate of an absolutely continuous path vanishes almost everywhere on its zero set. Thus **at almost every ray time** its velocity either has the displayed tangential form or no ray dwell occurs. Therefore \(\frac{d}{dt}|\rho-1|\leq-\lambda b^2|\rho-1|\) almost everywhere also at rays.

**3. Complete trajectories and global contraction.** The finite family of affine vector fields, and its convex hulls on finitely many rays, have a common linear-growth bound, giving forward existence and exclusion of finite-time escape for the Filippov differential inclusion. The continuous piecewise-linear gauge composed with a solution is absolutely continuous on finite intervals, so Grönwall's inequality applies:
\[
 |\rho(x(t))-1|\leq e^{-\lambda b^2t}|\rho(x(0))-1|.
\]
If \(\rho(x(0))>0\), the corresponding radial scalar dynamics is directed strictly away from \(\rho=0\) whenever \(0<\rho<1\), including all admissible sliding states. Thus a trajectory cannot reach the origin; the proof's ray normal-form is valid throughout. Since \(x/\rho(x)\in C\), and \(|x/\rho(x)|\leq1\) on the unit-circumradius polygon, 
\[
 \operatorname{dist}(x,C)\leq|x-x/\rho(x)|\leq|\rho(x)-1|.
\]
On \(C\), the normal terms vanish and the trajectory advances along each edge at the constant velocity \(\omega d_j\), requiring time \(1/\omega\) per edge. The vertex switching is transverse. This constructs the orbit with period \(N/\omega\). Any other nonconstant periodic solution with a nonzero point would satisfy the strict contraction over one period unless \(\rho\equiv1\), forcing it onto \(C\). No uniqueness claim is made for a solution starting exactly at the origin.

**4. Sliding residence and sharpness.** At a vertex ray with \(z>\omega/(\lambda a)\), the previous-sector transverse velocity is positive and the next-sector transverse velocity is negative. Thus both fields point towards the ray; the only forward solution there is the inward-pointing sliding solution until the threshold. On that interval, \(S=z^2\) obeys
\[
 \dot S=-2\lambda b^2 S-\frac{2\omega^2}{\lambda}.
\]
Integrating from \(z_0\) to \(\omega/(\lambda a)\) yields the stated positive time \(t_*\). For these trajectories the instantaneous relative decay of \(z\) initially equals \(\lambda b^2+\omega^2/(\lambda z_0^2)\). For every proposed uniform exponent \(c>\lambda b^2\), choose \(z_0\) sufficiently large that this is less than \(c\). Then the desired strengthened estimate with prefactor one is violated for all sufficiently small positive times. This proves optimality as claimed.

## Verification
The included `check.py` uses exact rational arithmetic for the polygon parameters at \(N=3,4,6\), including identities for the inward-pointing sliding fields, convex weights, relative dissipation, and endpoint signs, and tests the closed-form sliding residence against the integrated scalar equation. Execute `python3 check.py` from the extracted package. These finite checks corroborate algebra; the proof above supplies all-integer and all-initial-state quantifiers.

## Relationship to prior work
Kai [1], publicly available on 8 October 2026, constructs the polygonal oscillator and proves the prescribed polygon's existence and stability using sectorwise error dissipation and positively invariant polygonal annuli. Its switching convention is transversal hybrid flow rather than Filippov sliding and it does not state a universal sharp radial gauge contraction or explicit sliding residence law. Kai and Masuda [2,3] already address uniqueness of polygonal stable cycles in related switching systems, so the mere uniqueness or existence of a polygonal orbit is **not** advanced as new. Hanke and Stursberg [4] and Hanke, Liu, and Stursberg [5] prove globally stable cycles for other switched affine designs; their full-text conditions do not give the present exact regular-polygon Filippov sharp rate or sliding formula. The distinguishing assertion is the precise **Filippov completion, global optimal exponent, and computable attractive sliding transient** for the explicit regular-polygon source coefficients.

## Limitations
The conclusion assumes a regular polygon, constant positive \(\lambda,\omega\), and zero tangential perturbation \(\mu\). It excludes the origin. It characterizes **Filippov** solutions, not all hybrid trajectories under the source's different switching rule; changing the boundary convention can change behavior. The contraction exponent is optimal for a uniform prefactor-one bound, not necessarily the largest eventual asymptotic Lyapunov exponent for each individual trajectory. The 2011/2012 related Kai–Masuda full texts were not accessible despite lawful retrieval attempts, so a possibility of earlier equivalent quantitative statements cannot be fully excluded. The result has not undergone independent audit.

## References
[1] Tatsuya Kai, *Piecewise affine oscillators with polygonal limit cycles*, International Journal of Dynamics and Control 14, article 392 (first public 2026-10-08). https://doi.org/10.1007/s40435-026-02340-6

[2] Tatsuya Kai and S. Masuda, *A limit cycle synthesis method of multi-modal and 2-dimensional piecewise affine systems*, CDC (2011). https://doi.org/10.1109/CDC.2011.6160330

[3] Tatsuya Kai and S. Masuda, *Limit cycle synthesis of multi-modal and 2-dimensional piecewise affine systems*, Mathematical and Computer Modelling (2012). https://doi.org/10.1016/j.mcm.2011.08.028

[4] Nils Hanke and Olaf Stursberg, *On the Design of Limit Cycles of Planar Switching Affine Systems* (2023), https://arxiv.org/html/2303.16505v1

[5] Nils Hanke, Zonglin Liu, and Olaf Stursberg, *Synthesis of Limit Cycles and Reference Tracking via Switching Affine Systems* (2026), https://arxiv.org/html/2605.06181v1
