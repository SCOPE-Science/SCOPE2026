# Exact single-leader controllability and a conductance resonance on chorded cycles

## Finding

Consider the unweighted cycle with vertices \(0,1,\ldots,n-1\), \(n\ge4\), and add a chord from vertex \(0\) to vertex \(d\) of arbitrary conductance \(w>0\), where \(2\le d\le\lfloor n/2\rfloor\). Apply a single scalar input at vertex \(0\) to the continuous-time consensus dynamics \(\dot z=-Lz+e_0u\). Put \(m=n-d\) and \(g=\gcd(n,2d)\). Then the exact dimension of the unreachable subspace is

\[
\delta(n,d,w)=\left\lfloor\frac{g-1}{2}\right\rfloor+
\mathbf 1_{\{d,m\text{ even},\;w=1/d+1/m\}}.
\]

Equivalently, the Kalman controllability matrix has rank \(n-\delta(n,d,w)\). The first summand comprises chord-independent cycle sine modes. The second is a genuine conductance resonance: if both cycle arcs have even length, precisely the positive chord conductance \(w=1/d+1/m\) creates one additional unreachable eigenmode at Laplacian eigenvalue \(4\). The exceptional weight is also the reciprocal of the effective resistance \(d(n-d)/n\) between the chord endpoints in the original unit cycle. No other positive conductance produces an additional mode. In particular, the graph is controllable exactly when \(\gcd(n,2d)\le2\) and the exceptional indicator vanishes. For a unit-conductance chord, the exceptional case occurs only for \(n=4,d=2\).

## Assumptions and scope

All cycle edges have conductance one; the single new edge joins the nonadjacent vertices \(0\) and \(d\). The Laplacian is

\[
L=L(C_n)+w(e_0-e_d)(e_0-e_d)^\mathsf T.
\]

The input vector is \(e_0\), and ordinary real continuous-time controllability is intended. The same reachable subspace is obtained from \(I-hL\) for any nonzero scalar \(h\), but stability of such a discrete-time scheme is not asserted. Reflection of the cycle permits restricting \(d\) to the stated range. In the indicator, both \(d\) and \(m\) must be even; equivalently \(n\) and \(d\) are even.

## Proof

**Spectral reduction.** The symmetric-matrix Popov–Belevitch–Hautus criterion identifies the orthogonal complement of the reachable subspace with the span of Laplacian eigenvectors \(x\) satisfying \(x_0=0\). Since the graph is connected, eigenvalue \(0\) has only the constant eigenvector, and contributes nothing.

**All eigenvalues other than \(0\) and \(4\).** Fix such an eigenvalue \(\lambda\), choose possibly complex \(\theta\) with \(2-2\cos\theta=\lambda\) and \(\sin\theta\ne0\), and put \(q=x_d\). Along the two cycle arcs issuing from vertex \(0\), the eigenvalue recurrence gives

\[
x_j=A\sin(j\theta)\quad(0\le j\le d),\qquad
x_{n-j}=B\sin(j\theta)\quad(0\le j\le m),
\]

with endpoint consistency \(A\sin(d\theta)=B\sin(m\theta)=q\). These expressions remain valid for complex \(\theta\). Suppose first \(q\ne0\); then both endpoint sine factors are nonzero. The eigenvector equations at vertex \(0\) and at vertex \(d\), after dividing by \(q\), read

\[
w+\sin\theta\bigl(\csc(d\theta)+\csc(m\theta)\bigr)=0,
\]
\[
w+\sin\theta\bigl(\cot(d\theta)+\cot(m\theta)\bigr)=0.
\]

Subtracting and clearing their nonzero denominators yields

\[
\sin(d\theta)+\sin(m\theta)-\sin(n\theta)
=4\sin(n\theta/2)\sin(d\theta/2)\sin(m\theta/2)=0.
\]

The last two factors cannot vanish without an endpoint sine vanishing. Thus \(\sin(n\theta/2)=0\), which forces \(\theta=2\pi k/n\) for an integer \(k\). Consequently \(\sin(m\theta)=-\sin(d\theta)\), and the first displayed boundary equation reduces to \(w=0\), contrary to \(w>0\). Therefore \(q=0\).

Now \(x_0=q=0\). The vertex-\(0\) equation gives \(B=-A\), and a nonzero eigenvector requires \(A\ne0\). Endpoint consistency gives \(\sin(d\theta)=\sin(m\theta)=0\), so \(d\theta=r\pi\) and \(m\theta=s\pi\) for integers \(r,s\). The vertex-\(d\) equation says \(\sin((d-1)\theta)=\sin((m-1)\theta)\). Since \(\sin\theta\ne0\), this is equivalent to \((-1)^r=(-1)^s\). Hence \(n\theta=(r+s)\pi\) is an even multiple of \(\pi\). We may choose \(\theta=2\pi k/n\) with \(1\le k\le\lfloor(n-1)/2\rfloor\), and the endpoint condition becomes \(n\mid 2kd\). Conversely, for each such \(k\), the nonzero vector with components \(x_j=\sin(2\pi kj/n)\) is a cycle-Laplacian eigenvector, vanishes at both chord endpoints, and so is also an eigenvector of \(L\) orthogonal to \(e_0\). Different admitted \(k\) yield distinct eigenvalues, hence linearly independent modes. These are all the unreachable modes at \(\lambda\notin\{0,4\}\).

The allowed indices are exactly the positive multiples of \(n/g\) not exceeding \(\lfloor(n-1)/2\rfloor\). Their number is

\[
\left\lfloor\frac{\lfloor(n-1)/2\rfloor}{n/g}\right\rfloor
=\left\lfloor\frac{g-1}{2}\right\rfloor.
\]

**Exceptional eigenvalue \(4\).** At \(\lambda=4\), the recurrence along an arc with zero value at vertex \(0\) instead gives \(x_j=(-1)^{j-1}jA\) and \(x_{n-j}=(-1)^{j-1}jB\). If \(q=x_d=0\), endpoint consistency forces \(A=B=0\), so a nonzero mode has \(q\ne0\). Its two neighbors at vertex \(d\) are \(-q(d-1)/d\) and \(-q(m-1)/m\). The vertex-\(d\) equation therefore forces \(w=1/d+1/m\). The vertex-\(0\) equation, with \(A=(-1)^{d-1}q/d\) and \(B=(-1)^{m-1}q/m\), forces

\[
w=\frac{(-1)^d}{d}+\frac{(-1)^m}{m}.
\]

Equality with the required positive weight is possible only when both \(d\) and \(m\) are even. Conversely, in this parity case and at this unique weight, choose \(q=1\), set \(x_0=0\), \(x_d=1\), and set the components on the first and second arcs to \(x_j=(-1)^{j-d}j/d\) and \(x_{n-j}=(-1)^{j-m}j/m\), respectively. Direct substitution gives \(Lx=4x\), and the eigenvector space under \(x_0=0\) is one-dimensional because the two recurrences are determined by \(q\). This mode is independent of all earlier modes, which have eigenvalues strictly between \(0\) and \(4\). Summing the two contributions proves the rank formula.

## Verification

The accompanying `verify.py` builds the integer-scaled Laplacian for rational positive chord weights and computes the exact rank of its Krylov columns over a prime field. It checks 2,645 graph-and-weight configurations for \(4\le n\le48\), using unit, half-unit, three-half-unit, resonant, and twice-resonant conductances; it also verifies the displayed exceptional eigenvector by exact rational arithmetic. Run with `python3 verify.py` using the Python standard library. The finite-field ranks are reproducible computational cross-checks; the all-integer and all-real-weight assertions rest on the preceding proof, not on the finite experiments.

## Relationship to prior work

Parlangeli and Notarstefano (first posted 2011) develop the PBH and number-theoretic reachability theory for unmodified paths and cycles, including multiple inputs on a cycle. Their cycle theorem has a different graph and input configuration; it does not state the weighted single-chord classification or the isolated eigenvalue-\(4\) resonance. Liu and Lu (first posted 2014) derive Laplacian spectral formulas and spectral determination results for theta graphs, a class encompassing these chorded cycles, but do not formulate the leader controllability rank or positive-conductance resonance. General graph controllability-class criteria of Aguilar and Gharesifard (2015) do not provide these explicit parameters. A later closely related article of Liu and Ji (first published 2017) analyzes graphs constructed from paths and cycles; its full text was unavailable for definitive theorem-by-theorem comparison, so potential coverage remains a genuine literature risk.

## Limitations

This is a spectral and rank classification, not a quantitative controllability-Gramian or minimum-energy bound. The exact integer-weight conclusion is a specialization of a positive-real-weight theorem; zero or negative chord weights are outside scope. The originality assessment is a targeted literature comparison, not a proof that no equivalent result exists in an unindexed or inaccessible source. Independent validation has not been performed.

## References

- G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556v1 (first posted 2011-09-16); IEEE Transactions on Automatic Control 57 (2012), 743–748.
- X. Liu and P. Lu, *Laplacian spectral characterization of dumbbell graphs and theta graphs*, arXiv:1407.5255v1 (first posted 2014-07-20); Discrete Mathematics, Algorithms and Applications 8 (2016), 1650028.
- C. O. Aguilar and B. Gharesifard, *Graph Controllability Classes for the Laplacian Leader-Follower Dynamics*, IEEE Transactions on Automatic Control 60 (2015), 1611–1623; DOI:10.1109/TAC.2014.2381435.
- X. Liu and Z. Ji, *Controllability of multiagent systems based on path and cycle graphs*, International Journal of Robust and Nonlinear Control 28 (2018), 296–309; first online 2017-06-30; DOI:10.1002/rnc.3870.
