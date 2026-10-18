# Sharp fourth Fourier moment and complete phase rigidity for the centered hexagonal aperture

## Finding
Let \(S=\{(0,0),\pm(1,0),\pm(0,1),\pm(1,-1)\}\subset\mathbb Z^2\), and write \(P(z,w)=\sum_{v\in S}c_v z^{v_1}w^{v_2}\). Define \(M=\sum_{v\in S}|c_v|^2\). Then
\[
\int_{\mathbb T^2}|P|^4\,dm\le K M^2,
\qquad K=\frac{\rho^4+36\rho^2+48\rho+90}{(\rho^2+6)^2}=3.6562899693108\ldots,
\]
where \(\rho\) is the unique positive root of \(2\rho^3+6\rho^2-3\rho-12=0\). Equality for nonzero \(P\) holds exactly when \(c_{(0,0)}=\rho\lambda\) and \(c_v=\lambda\eta^{v_1}\xi^{v_2}\) for every nonzero \(v\in S\), with \(\lambda\ne0\) and \(|\eta|=|\xi|=1\). The same statement holds for uniform sampling on the square \(N\)-th-root grid for every integer \(N\ge5\). Modulo a nonzero common complex scalar, the optimizers form a two-dimensional torus.

## Assumptions and scope
Haar measure \(dm\) is probability measure on \(\mathbb T^2\). Coefficients are arbitrary complex numbers (zeros allowed). For the finite version use \(N^{-2}\sum_{j,k=0}^{N-1}|P(e^{2\pi i j/N},e^{2\pi i k/N})|^4\). The frequency support is contained in \(S\); equality forces support exactly \(S\). There is no claim about the sampled fourth moment for smaller \(N\).

## Proof
Step 1 (convolution and nonnegative reduction). Fourier orthogonality gives \(\int|P|^4=\sum_{u\in S+S}|\sum_{v+w=u}c_vc_w|^2\). Triangle inequality bounds this by the same expression with every coefficient replaced by its magnitude. Put \(a=|c_0|\) and denote the six noncentral magnitudes by \(x_v\), with \(R=\sum x_v^2\). Pair each root with its negative and write \(p_1=x_{(1,0)}x_{(-1,0)}\), \(p_2=x_{(0,1)}x_{(0,-1)}\), \(p_3=x_{(1,-1)}x_{(-1,1)}\). The direct convolution expansion is
\[
F=a^4+4a^2R+4a^2(p_1+p_2+p_3)+8aT+F_{\rm rim},
\]
where \(T\) is the sum of products \(x_u x_v x_w\) over the six unordered triples of distinct roots satisfying one of \(u+v=w\), \(u+w=v\), or \(v+w=u\). Direct enumeration of the zero-sum antipodal pair collisions gives
\[
F_{\rm rim}=2R^2-\sum_{v\ne0}x_v^4+8(p_1p_2+p_1p_3+p_2p_3).
\]

Step 2 (two exact rim estimates). Since \(p_1+p_2+p_3\le R/2\), \(\sum x_v^4\ge R^2/6\), and \(\sum_{i<j}p_i p_j\le(\sum_i p_i)^2/3\le R^2/12\), we obtain \(F_{\rm rim}\le(5/2)R^2\). Equality requires all six magnitudes equal.

For the cubic \(T\), group opposite pairs as \(X=(x_{(1,0)},x_{(-1,0)})\), \(Y=(x_{(0,1)},x_{(0,-1)})\), and \(Z=(x_{(1,-1)},x_{(-1,1)})\). Direct listing of the six root-addition triples gives
\[
T=X^{\mathsf T}\begin{pmatrix}z_1+z_2&z_1\\ z_2&z_1+z_2\end{pmatrix}Y.
\]
For \(\|Z\|_2=1\) and \(t=z_1z_2\in[0,1/2]\), the largest squared singular value of the displayed matrix is
\[
\frac{3+4t+\sqrt{5+16t+12t^2}}{2}\le\frac92.
\]
Therefore \(T\le(3/\sqrt2)\|X\|_2\|Y\|_2\|Z\|_2\le R^{3/2}/\sqrt6\). The last inequality uses arithmetic-geometric mean on the three squared block norms. Equality throughout holds exactly when all six \(x_v\) are equal and positive (apart from the all-zero case).

Step 3 (one-variable optimization). The previous inequalities imply
\[
F\le a^4+6a^2R+\frac8{\sqrt6}aR^{3/2}+\frac52 R^2.
\]
Writing \(R=6b^2\) for \(b\ge0\) gives \(F\le a^4+36a^2b^2+48ab^3+90b^4\). If \(b=0\) the quotient is \(1\); if \(a=0\) it is at most \(5/2\). For positive \(a,b\), put \(r=a/b\). The normalized quotient is \(Q(r)=(r^4+36r^2+48r+90)/(r^2+6)^2\) and
\[
Q'(r)=-\frac{24(2r^3+6r^2-3r-12)}{(r^2+6)^3}.
\]
The cubic is negative at zero, has a unique positive stationary minimum and then increases strictly to infinity, so it has one positive zero \(\rho\). Thus \(Q\) has its unique global maximum at \(\rho\). Its value exceeds both boundary quotients.

Step 4 (complex equality). Every upper-bound equality requires equal positive rim magnitudes. The convolution triangle inequalities must then have aligned phases for each two-sum. At sum zero this forces \(c_vc_{-v}/|c_vc_{-v}|=c_0^2/|c_0|^2\); at sums of the six root-addition triples it forces \(c_uc_v/|c_uc_v|=c_0c_w/|c_0c_w|\) whenever \(u+v=w\) in \(S\). Dividing by \(c_0\) and fixing the phases at \((1,0)\) and \((0,1)\) forces the coefficient phases to be the restriction of one character \((v_1,v_2)\mapsto\eta^{v_1}\xi^{v_2}\). Conversely these phases align every convolution fiber and attain all bounds.

Step 5 (finite grids). Every coordinate of an element of \(S+S\) is between \(-2\) and \(2\). When \(N\ge5\), reduction of \(S+S\) modulo \(N\) is injective; the sampled fourth moment is exactly the same two-sum convolution as above for all coefficient vectors. Hence the entire continuous theorem transports unchanged.

## Verification
Run `python verify.py` with Python 3 and SymPy installed. The standalone script recomputes the polynomial and derivative exactly, enumerates all six distinct root-addition triples, tests one hundred complex vectors, and checks exact convolution equality numerically on grids of orders \(5,6,7,9\). The recorded reproduction is `verification_output.txt`. The proof's singular-value bound is an explicit analytic calculation and does not depend on numerical sampling.

## Relationship to prior work
Ciccone and Gonçalves, arXiv:2208.09441 (first public 2022-08-19), prove a sharp Euclidean Fourier-extension inequality for functions on a geometric circle with an arithmetic condition on their one-dimensional Fourier-series supports, using Bessel estimates; that result does not compare the finite-dimensional \(\ell^2\)-to-torus-\(L^4\) norm on this seven-point planar lattice spectrum. González-Riquelme and Oliveira e Silva, arXiv:2405.16647 (first public 2024-05-26), prove sharp extension bounds on finite-field algebraic surfaces, a different underlying group, frequency geometry, and optimization problem. Nearby finite spectral calculations concern the six-point triangular aperture rather than this centered seven-point hexagon, and do not specify the algebraic constant or all optimizers here.

## Limitations
The result is a seven-mode, fourth-moment theorem and does not establish higher moments or stability bounds. Finite square grids of orders below five are not covered. Independent mathematical auditing has not been performed; a previously unindexed equivalent norm calculation remains possible.

## References
Ciccone, V.; Gonçalves, F. *Sharp Fourier Extension on the Circle Under Arithmetic Constraints*, arXiv:2208.09441, first submitted 19 August 2022. González-Riquelme, C.; Oliveira e Silva, D. *Sharp extension inequalities on finite fields*, arXiv:2405.16647, first submitted 26 May 2024.
