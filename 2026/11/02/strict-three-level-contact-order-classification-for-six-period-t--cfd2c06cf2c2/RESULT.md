# Strict three-level contact-order classification for six-period temporal SIS invasion on a path

## Finding

On a three-vertex path, suppose exactly one of the two edges is available at each of six recurring time steps, each edge appearing three times. Under the discrete-time independence mean-field SIS model below, the twenty possible schedules fall into precisely three equal-multiplier classes, with sizes six, twelve, and two. For every infection retention \(0<\alpha<1\) and transmission probability \(0<\beta<1\), their strict ordering is

\[
\rho(X^3Y^3)>\rho(X^2YXY^2)>\rho((XY)^3).
\]

The grouped schedule has the largest disease-free invasion multiplier, the alternating schedule the smallest, and every remaining schedule the intermediate multiplier. All six-step schedules use exactly the same number of contacts on each edge; their ordering alone changes the result. For \(\alpha=4/5\) and \(\beta=149/500\), the grouped and intermediate multipliers exceed one whereas the alternating multiplier is strictly below one. The example admits an exact rational certificate rather than a floating-point sign inference.

## Assumptions and scope

The vertex set is \(\{1,2,3\}\), with the only possible undirected edges \(\{1,2\}\) and \(\{2,3\}\). Each time step activates precisely one edge. A six-step word \(w\) has three symbols of each type, then repeats periodically. In the independence mean-field SIS probability recursion, let \(p_i(t)\) denote the infection probability at vertex \(i\), let \(\mu=1-\alpha\) denote recovery probability, and let \(N_i(t)\) contain the neighbors activated at time \(t\). The prescribed nonlinear recursion is

\[
p_i(t+1)=1-\bigl(1-\alpha p_i(t)\bigr)
             \prod_{j\in N_i(t)}\bigl(1-\beta p_j(t)\bigr).
\]

Its disease-free linearizations for activating the first or second edge, respectively, are

\[
X=\begin{pmatrix}\alpha&\beta&0\\\beta&\alpha&0\\0&0&\alpha\end{pmatrix},\qquad
Y=\begin{pmatrix}\alpha&0&0\\0&\alpha&\beta\\0&\beta&\alpha\end{pmatrix}.
\]

The product convention is left-to-right as a written word, and \(P_w\) denotes the matrix product in that convention. Reversing chronological multiplication reverses the word; this does not change its spectral radius in the present symmetric setting. Disease-free local exponential stability holds when \(\rho(P_w)<1\), while \(\rho(P_w)>1\) gives linear instability. This result makes no assertion at equality and does not equate mean-field instability with persistent infection in a finite stochastic SIS chain.

## Proof

**1. Word classification.** Rotating a word only cyclically permutes square matrix factors, hence preserves the characteristic polynomial. Since each factor is symmetric, reversing a word transposes its product and also preserves that polynomial. The twenty binary words of length six with three symbols of each type have exactly three orbits under rotations and reversal: \(XXXYYY\), containing six words; \(XXYXYY\), containing twelve; and \(XYXYXY\), containing two. Let \(G=X^3Y^3\), \(M=X^2YXY^2\), and \(A=(XY)^3\). The attached exact checker enumerates these twenty words, their orbits, and their characteristic polynomials.

**2. Characteristic-polynomial identities.** Write \(u=\alpha\), \(v=\beta\), and let \(p_W(z)=\det(zI-W)\). Direct multiplication gives

\[
\begin{aligned}
T_G&=3u^2(u^2+v^2)(u^2+3v^2),\\
T_M&=u^2(3u^4+12u^2v^2+5v^4),\\
T_A&=3u^2(u^4+4u^2v^2+v^4).
\end{aligned}
\]

All three products have determinant \(D=u^6(u^2-v^2)^6\). Expanding the second elementary symmetric coefficients, the constant terms cancel and the characteristic polynomials satisfy the exact identities

\[
\begin{aligned}
p_G(z)-p_M(z)&=-4u^2v^4z(z-K_{GM}),\\
p_M(z)-p_A(z)&=-2u^2v^4z(z-K_{MA}),
\end{aligned}
\]

where

\[
K_{GM}=u^2(u^4+3u^2v^2-v^4),\qquad
K_{MA}=u^2(u^4+3u^2v^2-\tfrac52v^4).
\]

The displayed formulas are polynomial identities for every positive \(u,v\); the checker verifies them symbolically.

**3. Strict Perron order.** Each product is entrywise nonnegative. For any nonnegative real \(3\)-by-\(3\) matrix \(W\), its Perron radius satisfies \(\rho(W)\ge\operatorname{tr}(W)/3\), because all eigenvalues have modulus at most \(\rho(W)\). Moreover,

\[
\begin{aligned}
\tfrac13T_M-K_{GM}&=u^2(u^2v^2+\tfrac83v^4)>0,\\
\tfrac13T_A-K_{MA}&=u^2(u^2v^2+\tfrac72v^4)>0.
\end{aligned}
\]

Consequently \(p_G(\rho(M))<p_M(\rho(M))=0\), and \(p_M(\rho(A))<p_A(\rho(A))=0\). A real monic characteristic polynomial is strictly positive beyond the spectral radius of its matrix: each real factor is positive beyond all real roots and each conjugate pair gives a positive quadratic factor. Therefore \(\rho(G)>\rho(M)>\rho(A)\). This argument does not require \(X\) or \(Y\) to be positive definite and holds across the entire parameter domain.

**4. Exact invasion-threshold separation.** Set \(u=4/5\), \(v=149/500\). At the slightly larger value \(v=3/10\), the positive vector \((5/4,3/2,1)^T\) is fixed by \(XY\). Reducing \(v\) to \(149/500\) makes every component of \(XY\) times this vector strictly smaller than the corresponding vector component. The positive-vector Collatz bound therefore gives \(\rho(XY)<1\), hence \(\rho(A)=\rho(XY)^3<1\). For the intermediate word, exact rational arithmetic yields

\[
\det(I-M)=-\frac{667551319210915426403604273201}{931322574615478515625000000000000}<0.
\]

A real monic characteristic polynomial cannot be negative at any real argument greater than or equal to the matrix spectral radius. Thus \(\rho(M)>1\). The strict ordering proved above implies \(\rho(G)>1\). This establishes a change in the linear invasion verdict caused only by contact ordering.

## Verification

Run `python checker.py` with SymPy installed. It verifies all three trace identities, the common determinant, the two characteristic-polynomial difference factorizations, both strict symbolic trace-to-threshold gaps, exhaustive enumeration of the twenty six-step words into three dihedral classes, equality of characteristic polynomials within each class, the exact positive-vector witness, and the negative rational value of \(\det(I-M)\). The infinite-parameter ordering is justified by the preceding algebra and Perron argument, not by a parameter grid.

## Relationship to prior work

Prakash, Tong, Valler, Faloutsos, and Faloutsos (2010) derive a matrix-product threshold framework for SIS processes on arbitrary time-varying graphs. Valdano, Ferreri, Poletto, and Colizza (initial arXiv version June 18, 2014; journal 2015) derive the infection-propagator spectral criterion for temporal SIS networks. Both frameworks include the relevant type of ordered factor product and are **not** presented as new here. The separate contribution assessed here is a complete, exact, rate-uniform ordering of all twenty balanced schedules on the simplest path with two competing edges, including a rational parameter choice at which the invasion verdict changes. Published general criteria by themselves do not assert these three classes or their strict order.

## Limitations

This is a local, mean-field invasion theorem for a particular periodically switched three-node path; it does not establish nonlinear endemic equilibria, epidemic peak sizes, finite-state stochastic persistence, a universal schedule order on larger networks, or robustness to arbitrary heterogeneous edge rates. The two source papers above were inspected directly; other prior matrix rearrangement results could subsume parts of the comparison. The earliest precisely dated motivating online preprint used for time classification is the June 18, 2014 arXiv version; the 2010 proceedings paper is earlier, but its first exact public day has not been established here. Independent scientific validation and historical-priority certification have not been performed.

## References

1. B. Aditya Prakash, H. Tong, N. Valler, M. Faloutsos, and C. Faloutsos (2010), *Virus Propagation on Time-Varying Networks: Theory and Immunization Algorithms*, ECML PKDD 2010, pp. 99–114, https://doi.org/10.1007/978-3-642-15939-8_7. Accessible full text: https://www.cs.cmu.edu/~christos/PUBLICATIONS/PKDD2010VirusProp.pdf.
2. E. Valdano, L. Ferreri, C. Poletto, and V. Colizza, *Analytical Computation of the Epidemic Threshold on Temporal Networks*, first arXiv posting June 18, 2014, https://arxiv.org/abs/1406.4815; *Physical Review X* 5 (2015), 021005, https://doi.org/10.1103/PhysRevX.5.021005.
3. E. Valdano, C. Poletto, and V. Colizza, *Infection propagator approach to compute epidemic thresholds on temporal networks: impact of immunity and of limited temporal resolution*, https://arxiv.org/abs/1510.07847 (October 27, 2015).
