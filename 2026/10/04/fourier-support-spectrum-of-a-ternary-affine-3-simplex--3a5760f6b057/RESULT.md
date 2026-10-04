# Fourier-support spectrum of a ternary affine 3-simplex
## Finding
For every integer \(d\ge3\), let \(u,v,w\in\mathbb F_3^d\) be linearly independent and let \(f:\mathbb F_3^d\to\mathbb C\) have support exactly \(x+\{0,u,v,w\}\), with all four support values nonzero. As those four nonzero values vary, the attainable Fourier-support sizes are exactly \[\{22,24,25,26,27\}\,3^{d-3}.\] Equivalently, after affine normalization the local polynomial \(P(X,Y,Z)=a_0+a_1X+a_2Y+a_3Z\), with \(a_0a_1a_2a_3\ne0\) and \(X,Y,Z\in\mu_3\), has exactly \(0,1,2,3\), or \(5\) zeros on \(\mu_3^3\), and each of these five zero counts occurs. In particular, \(23\,3^{d-3}\) is forbidden and the sharp fixed-support minimum is \(22\,3^{d-3}\).

## Assumptions and scope
Write \(\mu_3=\{1,\omega,\omega^2\}\), where \(\omega^2+\omega+1=0\). The four support points are required to be affinely independent: \(u,v,w\) are linearly independent over \(\mathbb F_3\). All four physical-space coefficients are nonzero. No claim is made for four-point supports of affine rank two, or for other fields.

Translation of the support only multiplies the Fourier transform by a nonvanishing character. An invertible linear change of variables sends \(u,v,w\) to the first three coordinate vectors and permutes the dual group. Hence it suffices to study
\[
P(X,Y,Z)=a_0+a_1X+a_2Y+a_3Z,
\qquad (X,Y,Z)\in\mu_3^3,
\]
with \(a_0a_1a_2a_3\ne0\). Every triple \((X,Y,Z)\) occurs exactly \(3^{d-3}\) times among the characters of \(\mathbb F_3^d\).

## Proof
It remains to classify the number of zeros of \(P\) on the twenty-seven-point character cube \(\mu_3^3\). Associate to each grid point the evaluation row
\[
r(X,Y,Z)=(1,X,Y,Z)\in\mathbb Q(\omega)^4.
\]
A zero of \(P\) is a row orthogonal to the coefficient vector \((a_0,a_1,a_2,a_3)\).

The finite classification is exact over the Eisenstein field \(\mathbb Q(\omega)\). First, every four distinct evaluation rows have rank at least three. Thus any hyperplane containing at least four grid points contains three linearly independent evaluation rows. Three independent rows determine the coefficient vector up to scale by the four signed \(3\times3\) cofactors. Enumerating all \(\binom{27}{3}=2925\) triples exactly, discarding the rank-at-most-two triples and then requiring all four cofactors to be nonzero, gives only two possible intersection sizes for the corresponding hyperplane: three or five grid points. More precisely, there are 2862 rank-three triples; 864 give a cofactor vector with all four entries nonzero; among those, 216 triples determine a three-point zero set and 648 determine a five-point zero set. Consequently an admissible \(P\) can never have four zeros or more than five zeros.

The remaining zero counts are attained by explicit real coefficient vectors. In the order \((a_0,a_1,a_2,a_3)\), the vectors
\[
(1,1,1,1),\quad(-3,-1,2,2),\quad(-3,-3,-2,-1),\quad(-3,-2,2,3),\quad(-1,-1,1,1)
\]
have respectively \(0,1,2,3,5\) zeros on \(\mu_3^3\). All coefficients are nonzero. Therefore the local Fourier-support sizes are exactly \(27,26,25,24,22\), and multiplying by \(3^{d-3}\) proves the stated spectrum in every dimension \(d\ge3\).

## Verification
The accompanying `verify.py` performs the finite step using exact Eisenstein-integer arithmetic, representing \(a+b\omega\) by the integer pair \((a,b)\). It checks all \(\binom{27}{4}=17550\) four-row subsets for rank at least three, checks every three-row cofactor hyperplane, verifies the intersection-count census \(216\) versus \(648\), and verifies all five explicit witnesses. It uses no floating-point arithmetic and prints `VERIFY_OK` only after every assertion passes.

## Relationship to prior work
Delvaux and Van Barel study rank-deficient submatrices of Kronecker products of Fourier matrices and their Hamming numbers. Their 2006 report treats \(F=F_{n_1}\otimes\cdots\otimes F_{n_k}\), gives global Hamming-number bounds and constructions, and explicitly notes that those results do not characterize uniqueness of the rank-deficient submatrices. For order \(27\), their global Hamming-number theory concerns the minimum over all four-column supports; it does not determine the complete Fourier-support spectrum for the prescribed affine-independent four-column geometry used here.

Bonami and Ghobber study equality cases for support-spectrum uncertainty on \(\mathbb Z_p\times\mathbb Z_p\), \(\mathbb Z_{p^2}\), and \(\mathbb Z_p\times\mathbb Z_q\). Their framework concerns cardinality-minimal spectra and does not cover the rank-three group \(\mathbb F_3^3\) or the complete spectrum for a fixed affine 3-simplex.

## Limitations
The theorem is specific to the unique affine-rank-three geometry of a four-point support over \(\mathbb F_3\). It does not classify affine-rank-two supports, larger supports, other primes, or weighted notions of Fourier concentration. The local hyperplane classification is finite and exact; the computational certificate proves that finite classification, while the reduction from arbitrary \(d\ge3\) is analytic. A residual literature risk is that the same twenty-seven-point hyperplane-section spectrum may occur under coding-theoretic or finite-geometric terminology not identified by the searches used here.

## References
1. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, Report TW 477, K.U. Leuven, 15 November 2006. Primary AMS classification 42A99. https://www.cs.kuleuven.be/publicaties/rapporten/tw/TW477.pdf
2. A. Bonami and S. Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060, first submitted 26 March 2010. https://arxiv.org/abs/1003.5060
