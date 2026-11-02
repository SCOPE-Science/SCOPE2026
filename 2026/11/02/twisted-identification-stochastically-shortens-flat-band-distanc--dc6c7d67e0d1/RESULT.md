# Twisted identification stochastically shortens flat-band distances with a fourth-order threshold

## Finding
For any positive length \(L\) and width \(H\), form two compact Euclidean flat surfaces from the rectangle \([0,L]\times[-H/2,H/2]\): the cylinder \(C_{L,H}\) identifies \((0,y)\sim(L,y)\), while the Möbius band \(M_{L,H}\) identifies \((0,y)\sim(L,-y)\). Equip each with its intrinsic shortest-path metric and normalized area measure. Let \(D_C\) and \(D_M\) denote the distances between two independent area-uniform points in the corresponding surfaces.

**Theorem.** The Möbius distance is stochastically dominated by the cylinder distance:
\[
\mathbb P(D_M>t)\le\mathbb P(D_C>t)\quad\text{for every }t\ge0.
\]
The distributions are different for every \(L,H>0\). In particular, \(\mathbb E[D_M^p]<\mathbb E[D_C^p]\) for every \(p>0\).

Writing \(\Delta(L,H)=\mathbb E[D_C^2]-\mathbb E[D_M^2]\), the **exact twist defect** is
\[
\boxed{\Delta(L,H)=
\begin{cases}
\dfrac{H^4}{36L^2},&0<H\le L,\\[5pt]
\dfrac{H^2}{8}-\dfrac{L^2}{4}
+\dfrac{11L^4}{72H^2}
+\dfrac{L^4}{6H^2}\log\!\left(\dfrac HL\right),&H>L.
\end{cases}}
\]
Also \(\mathbb E[D_C^2]=L^2/12+H^2/6\), so this determines \(\mathbb E[D_M^2]\) exactly. The normalized defect
\[
\mathcal R(H/L)=\frac{\Delta(L,H)}{L^2/12+H^2/6}
\]
is strictly increasing in the aspect ratio \(H/L\), from limit \(0\) at aspect ratio zero to limit \(3/4\) at aspect ratio infinity. For fixed \(L\), the defect is \(C^3\) but not \(C^4\) at \(H=L\). More precisely, for \(h\downarrow0\),
\[
\Delta(L,L+h)=\frac{(L+h)^4}{36L^2}-\frac{h^4}{3L^2}+O_L(h^5),
\]
whereas the first term is the exact expression when \(-L<h\le0\). Thus the one-sided fourth derivative changes by \(-8/L^2\).

## Assumptions and scope
Both metrics are the **intrinsic quotient metrics** of the Euclidean strip, not distances in a particular three-dimensional embedding. The quotient has its inherited boundary. Area-uniform sampling means normalized two-dimensional Riemannian area; the seam and boundary carry zero sampling mass. Both \(L\) and \(H\) are strictly positive, and both points are sampled independently. No embedding or aspect-ratio feasibility restriction is assumed.

## Proof
**1. Exact distances on both quotients.** Choose independent representatives \((X_i,Y_i)\) with \(X_i\) uniform on \([0,L]\) and \(Y_i\) uniform on \([-H/2,H/2]\). Put \(a=|X_1-X_2|\). The universal covering strip is convex, so a shortest path is a straight segment to an appropriate deck translate. The nearest even translate of the Möbius deck action has horizontal distance \(a\) and vertical difference \(Y_1-Y_2\); the nearest odd translate has horizontal distance \(L-a\) and vertical difference \(Y_1+Y_2\). All other translates have at least as great a horizontal displacement with the same parity. Therefore
\[
D_M^2=\min\{a^2+(Y_1-Y_2)^2,\ (L-a)^2+(Y_1+Y_2)^2\},
\]
whereas
\[
D_C^2=\min\{a,L-a\}^2+(Y_1-Y_2)^2.
\]

**2. Exact monotone coupling.** To construct a cylinder sample on the same probability space as the Möbius sample, retain \(X_1,X_2,Y_1\) and replace \(Y_2\) by \(Y_2\) if \(a\le L/2\), and by \(-Y_2\) otherwise. The transformed coordinate remains independent and uniform because its conditional law is symmetric. The cylinder squared distance in this coupling is exactly the Möbius branch with the smaller horizontal length. The Möbius distance is the minimum of that branch and the competing branch, so \(D_M\le D_C\) pointwise in the coupling. Since the competing branch is strictly shorter with positive probability when \(H>0\), the two distributions differ. The coupling implies strict inequalities for all positive increasing powers of distance.

**3. A uniform horizontal energy gap.** Let \(b=\min\{a,L-a\}\) and \(\Xi=(L-b)^2-b^2=2L|a-L/2|\). The density of \(a\) is \(2(L-a)/L^2\), and folding around \(L/2\) shows that \(\Xi\) is exactly uniform on \([0,L^2]\). After the conditional reflection in Step 2, the difference of the two vertical squared terms has the distribution of \(4Y_1Y_2\), independently of \(\Xi\). Consequently the **squared-distance improvement in the explicit coupling** obeys
\[
D_C^2-D_M^2\ \stackrel{\mathrm{law}}=\ (H^2 Z_1Z_2-\Xi)_+,
\]
where \(Z_1,Z_2\) are independent uniform variables on \([-1,1]\), \(\Xi\) is independent uniform on \([0,L^2]\), and \(u_+=\max\{u,0\}\). This distributional identity proves the exact uniform-gap reduction without an assumption of independence between the two original vertical squared distances.

**4. Exact integration.** Let \(r=H/L\). With
\[
F(s)=\int_0^1(s-v)_+\,dv=\begin{cases}0&s\le0,\\s^2/2&0<s\le1,\\s-1/2&s\ge1,\end{cases}
\]
Step 3 gives \(\Delta(L,H)=L^2\mathbb E[F(r^2Z_1Z_2)]\). The positive part of the product has mass \(1/2\), and, conditioned on positivity, its density on \((0,1)\) is \(-\log z\). Thus
\[
\Delta(L,H)=\frac{L^2}{2}\int_0^1F(r^2z)(-\log z)\,dz.
\]
When \(r\le1\), use \(\int_0^1z^2(-\log z)\,dz=1/9\), obtaining \(H^4/(36L^2)\). When \(r>1\), separate the integral at \(z=r^{-2}\). Equivalently, evaluate
\[
I(\lambda)=\int_{\lambda}^1(z-\lambda)^2(-\log z)\,dz
=\frac19-\frac\lambda2+\lambda^2-\frac{11\lambda^3}{18}+\frac{\lambda^3\log\lambda}{3},
\quad \lambda=r^{-2},
\]
which yields the stated second branch. For the cylinder, \(\min\{a,L-a\}\) is uniform on \([0,L/2]\), giving mean squared horizontal distance \(L^2/12\); independently \(\mathbb E[(Y_1-Y_2)^2]=H^2/6\).

**5. Strict normalized monotonicity and limits.** Put \(s=r^2\). For each fixed \(z>0\), the function \(F(sz)/(1+2s)\) increases strictly with \(s>0\): before \(sz=1\) it equals \(s^2z^2/[2(1+2s)]\), and after the threshold it equals \((sz-1/2)/(1+2s)\); differentiating either expression gives a strictly positive derivative. Since \(\mathbb P(Z_1Z_2>0)=1/2\), the formula \(\mathcal R(r)=12\mathbb E[F(r^2Z_1Z_2)]/(1+2r^2)\) is strictly increasing. It tends to zero as \(r\downarrow0\). As \(s\to\infty\), \(F(sz)/s\to z_+\) and is bounded by \(z_+\), so dominated convergence and \(\mathbb E[(Z_1Z_2)_+]=1/8\) give \(\lim_{r\to\infty}\mathcal R(r)=3/4\).

**6. Sharp fourth-order transition.** At \(r=1\), the integration interval where \(r^2z>1\) opens for the first time. Setting \(\lambda=r^{-2}\), the density \(-\log z=(1-z)+O((1-z)^2)\) gives \(I(\lambda)=(1-\lambda)^4/12+O((1-\lambda)^5)\). For \(H=L+h\) with \(h>0\), this changes the polynomial branch by \(-h^4/(3L^2)+O_L(h^5)\). Thus derivatives through order three match and the fourth derivative has the claimed jump. No finite numerical experiment is used as proof of these identities.

## Verification
Run `python3 checks/verify_twist.py` in an environment with the version of NumPy in `requirements.txt`. The script evaluates the original geometric minimum directly by a three-variable Gauss–Legendre quadrature, separately verifies the untwisted cylinder moment, performs seeded independent sampling from both quotient surfaces, checks the exact rational small-width formula, examines the fourth-order onset coefficient, and samples the strictly monotone normalized profile. Exact symbolic steps in the proof (in particular the integral for \(I\) and the monotone-coupling argument) do not depend on the numerical checks.

## Relationship to prior work
The notion of an unlabeled pair-distance distribution and its inverse-geometric applications are developed by Mémoli and Needham (arXiv:1810.09646; published 2022). Schwartz (arXiv:2308.12641) studies the **extrinsic isometric-embedding** aspect-ratio problem for flat Möbius bands and uses the same abstract rectangular quotient as input; those embedding restrictions are not assumed here. Cui, Hauck, Fabian and Koeppl (ICLR 2024, Appendix A) explicitly use the intrinsic twisted-quotient distance in a multi-agent experiment; that **forward distance formula is prior art**. The present claim is the comparison of its entire random pair-distance law with the untwisted quotient, together with the exact two-branch squared-distance defect, its strict normalized monotonicity, and the sharp fourth-order transition. This is not an embedding theorem or a claim to originate the quotient metric formula. The 2018/2022 paper's abstract and references were accessible but its full text was not accessible during the comparison, leaving priority uncertainty explicitly unresolved.

## Limitations
The result concerns rectangular **flat** metric quotients and area-uniform independent pairs. Stochastic dominance does not assert a strict CDF inequality at every distance threshold. It supplies no finite-sample confidence bounds and no analogous theorem for nonuniform sampling or nonflat embedded metrics. The transition is a statement about the second intrinsic distance moment, not about an extrinsic bending energy. Historical novelty remains provisional until broader archival and independent review.

## References
1. F. Mémoli and T. Needham, *Distance distributions and inverse problems for metric measure spaces*, arXiv:1810.09646 (first posted 2018-10-23); *Studies in Applied Mathematics* 149 (2022), 943–1001. https://arxiv.org/abs/1810.09646 ; https://doi.org/10.1111/sapm.12526 .
2. R. E. Schwartz, *The Optimal Paper Moebius Band*, arXiv:2308.12641 (first posted 2023-08-24), especially §1.2 and §3.4. https://arxiv.org/abs/2308.12641 .
3. K. Cui, S. Hauck, C. Fabian and H. Koeppl, *Learning Decentralized Partially Observable Mean Field Control for Artificial Collective Behavior*, ICLR 2024, Appendix A, p. 15 (the flat Möbius quotient distance). https://proceedings.iclr.cc/paper_files/paper/2024/file/b28ca52a43881fd87196c71145f30092-Paper-Conference.pdf .
