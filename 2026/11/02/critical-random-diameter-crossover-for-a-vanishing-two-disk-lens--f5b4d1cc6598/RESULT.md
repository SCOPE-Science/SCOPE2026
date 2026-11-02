# Critical random-diameter crossover for a vanishing two-disk lens

## Finding
For fixed \(\lambda\ge0\), intersect the two unit disks with centers \((\pm\lambda n^{-4/5},0)\), and choose \(n\) independent points uniformly by area from the resulting lens. Write \(M_n\) for their maximum pairwise Euclidean distance and \(s_n=n^{-4/5}\). Then for every \(t\ge0\),
\[
\Pr\big\{s_n^{-1}(2-M_n)\le t\big\}\longrightarrow 1-\exp[-\Lambda_\lambda(t)],
\quad\Lambda_\lambda(t)=\frac8{15\pi^2}\int_0^{2\pi}(t-2\lambda|\cos\theta|)_+^{5/2}\,d\theta.
\]
For \(t<0\) the limiting probability is zero. Here \((x)_+=\max\{x,0\}\). The entire limiting family is explicit. In particular,
\[
\Lambda_0(t)=\frac{16}{15\pi}t^{5/2},\qquad
\Lambda_\lambda(t)\sim\frac{32}{105\pi^2\lambda}t^{7/2}\ (t\downarrow0,\ \lambda>0),\qquad
\Lambda_\lambda(t)\sim\frac{16}{15\pi}t^{5/2}\ (t\to\infty).
\]
For every positive \(\lambda\), the limit law is **not** Weibull; the first transition of contributing antipodal orientation angles is at \(t=2\lambda\). At \(\lambda=0\), the law specializes to the known disk maximal-distance law.

## Assumptions and scope
The ambient space is the Euclidean plane. \(B_2(z,1)\) is the closed unit disk centered at \(z\). For every fixed real \(\lambda\ge0\), take all sufficiently large integers \(n\ge2\) for which \(c_n=\lambda n^{-4/5}<1\). Define
\[
K_n=B_2((-c_n,0),1)\cap B_2((c_n,0),1),\qquad M_n=\max_{1\le i<j\le n}|X_{n,i}-X_{n,j}|,
\]
where \(X_{n,1},\dots,X_{n,n}\) are independent and area-uniform in \(K_n\). Rows need not be coupled across \(n\). The lens has exact geometric diameter \(2\sqrt{1-c_n^2}=2+O_\lambda(n^{-8/5})\), hence centering at \(2\) is equivalent at the theorem's scale to centering at the true lens diameter. The claim is only for fixed \(\lambda\), not varying or diverging \(\lambda_n\).

## Proof
Set \(s=n^{-4/5}\) and \(c=\lambda s\). The radial boundary of \(K_n\), measured from the origin, is
\[
\rho_c(\theta)=\sqrt{1-c^2\sin^2\theta}-c|\cos\theta|=1-\lambda s|\cos\theta|+O_\lambda(s^2)
\]
uniformly in \(\theta\). Its area is \(A_c=2\arccos(c)-2c\sqrt{1-c^2}=\pi+O_\lambda(s)\). For fixed \(t>0\), a pair with distance exceeding \(2-st\) must have both radial coordinates at least \(1-st\), and its angular separation is \(\pi+O_t(\sqrt{s})\); this follows respectively from the triangle inequality and the cosine law. Thus every contributing pair has a unique representation (up to negligible angular seams)
\[
\begin{aligned}
 r_1&=\rho_c(\theta)-su_1,&r_2&=\rho_c(\theta+\pi+\sqrt{s}z)-su_2,\\
 \theta_1&=\theta,&\theta_2&=\theta+\pi+\sqrt{s}z,
\end{aligned}
\]
with \(u_1,u_2\ge0\) and \(u_1,u_2,|z|\) uniformly bounded on the event. Expanding the cosine law, uniformly on these compact parameter ranges,
\[
\frac{2-|X_{n,1}-X_{n,2}|}{s}=
2\lambda|\cos\theta|+u_1+u_2+\frac{z^2}{4}+o(1).
\]
The polar Jacobian for two independent uniform area points, together with the changes \(r_i\mapsto u_i\) and \(\theta_2\mapsto z\), is \((1+o(1))s^{5/2}\,du_1du_2dzd\theta/\pi^2\). Dominated convergence therefore gives
\[
\begin{aligned}
 p_n(t)&:=\Pr\big\{|X_{n,1}-X_{n,2}|>2-st\big\}\\
 &=\frac{s^{5/2}}{\pi^2}\int_0^{2\pi}\int_{\substack{u_1,u_2\ge0,\ z\in\mathbb R\\u_1+u_2+z^2/4<t-2\lambda|\cos\theta|}}du_1du_2dz\,d\theta+o(s^{5/2})\\
 &=\frac{16s^{5/2}}{15\pi^2}\int_0^{2\pi}(t-2\lambda|\cos\theta|)_+^{5/2}d\theta+o(s^{5/2}),
\end{aligned}
\]
where the elementary inner integral is \(16a^{5/2}/15\) for \(a\ge0\). Since \(n^2s^{5/2}=1\), the expected number \(W_n(t)\) of unordered pairs exceeding \(2-st\) tends to \(\Lambda_\lambda(t)\).

For completeness, we prove Poisson convergence rather than treating the \(\binom n2\) pair distances as independent. Expand each fixed factorial moment of \(W_n(t)\) as a sum over ordered collections of distinct unordered edges on the \(n\) sample labels. A collection of disjoint edges contributes the corresponding power of \(\Lambda_\lambda(t)\). For a connected component on \(v\ge3\) distinct labels, the near-diameter restriction forces all \(v\) points into radial boundary strips of thickness \(O_t(s)\), and every edge of a spanning tree forces its new vertex into an angular window \(O_t(\sqrt s)\) around the antipode of the earlier one. Hence the joint occurrence probability is at most
\[
O_{t,\lambda}\bigl(s^{v+(v-1)/2}\bigr)=O_{t,\lambda}\bigl(s^{(3v-1)/2}\bigr).
\]
After summing over label choices, such a component costs
\[
O_{t,\lambda}\bigl(n^v s^{(3v-1)/2}\bigr)=O_{t,\lambda}\bigl(n^{(2-v)/5}\bigr)=o(1).
\]
Every non-disjoint edge collection contains at least one such component, while other components contribute bounded factors. Thus all factorial moments converge to those of a Poisson variable of mean \(\Lambda_\lambda(t)\), yielding \(W_n(t)\Rightarrow\mathrm{Poisson}(\Lambda_\lambda(t))\). The desired cumulative limit is
\[
\Pr\big\{s^{-1}(2-M_n)\le t\big\}=\Pr\{W_n(t)\ge1\}\longrightarrow1-e^{-\Lambda_\lambda(t)}
\]
for \(t>0\). At \(t=0\), the limiting distribution is zero by monotonicity and continuity. The event is impossible for \(t<0\), since every interpoint distance is at most \(2\).

For \(\lambda=0\), the angular integral is \(2\pi t^{5/2}\), giving the known disk coefficient. For \(\lambda>0\), the permitted angles are those with \(|\cos\theta|<t/(2\lambda)\); they fill the circle up to the two null directions at \(t=2\lambda\). As \(t\downarrow0\), linearizing \(|\cos\theta|\) near its two zeros yields
\[
\int_0^{2\pi}(t-2\lambda|\cos\theta|)_+^{5/2}d\theta\sim\frac{4}{7\lambda}t^{7/2}.
\]
For large \(t\), the same integral is \(2\pi t^{5/2}(1+O(\lambda/t))\). These different small- and large-\(t\) powers rule out every pure Weibull cumulative law for \(\lambda>0\).

## Verification
The radial formula follows by solving \(r^2+2cr|\cos\theta|+c^2\le1\). Direct integration over \((u_1,u_2,z)\) gives \(16a^{5/2}/15\). The constant at \(\lambda=0\), \(16/(15\pi)\), independently matches Mayer–Molchanov's unit-disk formula. The bundled `verify.py` numerically integrates the intensity and compares a seeded Monte Carlo simulation using convex-hull diameters at two parameters; finite-\(n\) simulations exhibit expected convergence bias and are not a proof of the theorem. The analytic derivation above proves every asymptotic claim.

## Relationship to prior work
Appel, Najim and Russo (2002) study maximum interpoint distances for **fixed** planar sampling regions, and Mayer and Molchanov (2006) prove a general extremal-pair Poisson method and the limiting law for a **fixed** unit ball. Those results motivate this theorem's normalization and method, and the present limit reduces exactly to their disk limit at \(\lambda=0\). Jammalamadaka and Janson (2015) likewise study fixed spherically symmetric sampling laws. The distinct statement here concerns a critical **triangular array of shrinking two-disk intersections**, yielding a non-Weibull interpolation with a new explicit angular crossover. The fixed-region and fixed-sampling-law theorems do not directly imply this parameter-dependent intensity. The fixed-lens chord-length literature (Harutyunyan 2011) concerns a different, single-line statistic and does not evaluate the sample-maximal diameter at a vanishing lens separation.

## Limitations
The theorem does not cover a fixed nonzero center displacement, a diverging rescaled displacement, arbitrary lens radii, higher dimensions, or rates of convergence. Prior papers provide much of the Poisson-extremes machinery; no claim of novelty is made for that general technique or for the disk endpoint. A search and reading of highly relevant literature cannot exclude an equivalent result in an undiscovered source; the 2002 paper's full text was not available for inspection, although its fixed-body scope is documented and reiterated in the later primary literature. The Monte Carlo checks are finite and supplementary.

## References
1. M. Mayer and I. Molchanov, *A limit theorem for the maximal interpoint distance of a random sample in the unit ball*, preprint first posted 2006-05-11, arXiv:math/0605289, https://arxiv.org/pdf/math/0605289.
2. M. J. B. Appel, C. A. Najim and R. P. Russo, *Limit laws for the diameter of a random point set*, Advances in Applied Probability 34 (2002), 1–10, DOI 10.1239/aap/1019160946.
3. S. R. Jammalamadaka and S. Janson, *Asymptotic distribution of the maximum interpoint distance in a sample of random vectors with a spherically symmetric distribution*, Annals of Applied Probability 25 (2015), DOI 10.1214/14-AAP1082.
4. H. Harutyunyan, *Chord Length Distribution Function for Lens*, 2011.
5. M. Schulte and C. Thäle, *U-max-statistics*, Journal of Multivariate Analysis 99 (2008), DOI 10.1016/j.jmva.2008.02.001.
