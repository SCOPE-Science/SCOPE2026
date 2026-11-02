# Exact logarithmic graph-tube law and Bernoulli structure of the geometric fractal tent map

## Finding
For each fixed \(0<q<1\), set \(d=(1-q)/2\) and consider the countably piecewise-affine fractal tent map defined below. Let \(\Gamma_q\) be the closure in \(\mathbb R^2\) of its open-branch graph, and let \((\Gamma_q)_\varepsilon\) denote its open Euclidean \(\varepsilon\)-neighborhood. Then
\[
\boxed{\operatorname{area}((\Gamma_q)_\varepsilon)
 =\frac{4\varepsilon}{\log(1/q)}\log(1/\varepsilon)
  +O_q(\varepsilon),\qquad\varepsilon\downarrow0.}
\]
In particular both lower and upper box dimensions and the Hausdorff dimension of \(\Gamma_q\) are exactly \(1\), even though its one-dimensional Hausdorff measure is infinite. The sharp logarithmic factor explains why finite-resolution graph measurements can suggest a noninteger box dimension.

For the same map, Lebesgue measure on \([0,1]\) is invariant and its symbolic branch itinerary is a countable independent-and-identically-distributed process. The measure-theoretic entropy and almost-sure Lyapunov exponent are both
\[
\boxed{h_\lambda(F_q)=\int_0^1\log |F'_q(x)|\,dx
= -\log\!\left(\frac{1-q}{2}\right)
-\frac{q}{1-q}\log q.}
\]
The two statements describe the same geometrically scaled full-branch system: a finite entropy rate coexists with a graph having infinitely many unit-height affine pieces and a logarithmically divergent tube-length normalization.

## Assumptions and scope
Fix a real \(q\in(0,1)\). Write
\[
d=\frac{1-q}{2},\qquad w_j=dq^j,\qquad s_j=\frac{1-q^j}{2},\qquad j=0,1,2,\ldots.
\]
The open left branches are \(I_j^L=(s_j,s_j+w_j)\), and the open right branches are \(I_j^R=(1-s_j-w_j,1-s_j)\). They partition \((0,1)\) up to their countable endpoints and the accumulation point \(1/2\). Define
\[
F_q(x)=\begin{cases}
(x-s_j)/w_j,&x\in I_j^L,\\[2pt]
(1-s_j-x)/w_j,&x\in I_j^R.
\end{cases}
\]
Extend this Borel map at the countable exceptional points in any measurable manner taking values in \([0,1]\). The geometric and measure-theoretic assertions concern \(\Gamma_q\), the closure of all open-branch line segments, and are independent of the exceptional-point extension. This is the branch-search rule of Kopets et al. on their geometric-balance locus \(1-q=2d\); the variables correspond to their parameters \(K=q\) and \(D=d\).

The neighborhood is taken in the entire Euclidean plane, not clipped to the unit square. The remainder \(O_q(\varepsilon)\) is for each fixed \(q\), without uniformity as \(q\) approaches \(0\) or \(1\). Entropy means Kolmogorov--Sinai entropy of the Lebesgue-preserving interval map, not finite-precision output entropy or topological entropy of a discontinuous map.

## Proof
**1. Exact branches and invariant measure.** The identity \(s_{j+1}-s_j=w_j\), together with \(\sum_{j\ge0}w_j=d/(1-q)=1/2\), shows that the two families fill the left and right half-intervals up to null boundary sets. Every branch is an affine bijection onto \((0,1)\) with absolute derivative \(1/w_j\). Hence for every Borel set \(E\subseteq(0,1)\),
\[
\lambda(F_q^{-1}E)=\sum_{j\ge0}\bigl(w_j\lambda(E)+w_j\lambda(E)\bigr)=\lambda(E).
\]
A branch cylinder with successive labels \((\sigma_0,j_0),\ldots,(\sigma_{n-1},j_{n-1})\), \(\sigma_i\in\{L,R\}\), has Lebesgue measure \(\prod_{i=0}^{n-1}w_{j_i}\). Indeed each affine inverse branch scales lengths by \(w_j\); composition gives the product. As \(\max_jw_j=d<1\), cylinder diameters tend to zero. Thus branch coding is a measure-theoretic isomorphism, modulo a null exceptional set, to the one-sided Bernoulli shift with single-letter weights \(w_j\) for each of the two orientations. Its entropy is the finite Shannon series
\[
-2\sum_{j\ge0}w_j\log w_j
=-\log d-\frac{q}{1-q}\log q.
\]
The branchwise logarithmic derivative has the same integral, and the Bernoulli ergodic theorem gives the almost-sure Lyapunov exponent.

**2. Graph closure.** For each \(j\), the left and right graph pieces are the line segments parametrized by
\[
P_j^L(y)=(s_j+w_jy,y),\qquad
P_j^R(y)=(1-s_j-w_jy,y),\qquad 0\le y\le1.
\]
Their closure additionally includes the full segment \(\{1/2\}\times[0,1]\), since \(s_j\uparrow1/2\) and \(w_j\downarrow0\). There are no other accumulation pieces. Each of the countably many open graph pieces has Euclidean length \(\sqrt{1+w_j^2}\ge1\); their pairwise disjoint interiors show that \(\mathcal H^1(\Gamma_q)=\infty\). As \(\Gamma_q\) is a countable union of line segments, \(\dim_H\Gamma_q=1\).

**3. Upper Euclidean neighborhood estimate.** Let \(N_+(\varepsilon)\) be the least nonnegative integer with \(q^{N_+}\le\varepsilon\). The \(\varepsilon\)-neighborhood of a single segment of length \(\sqrt{1+w_j^2}\) has area \(2\varepsilon\sqrt{1+w_j^2}+\pi\varepsilon^2\). For the first \(N_+\) pairs of graph segments, subadditivity therefore bounds the area by
\[
4\varepsilon\sum_{j<N_+}\sqrt{1+w_j^2}+2\pi N_+\varepsilon^2
=4\varepsilon N_++O_q(\varepsilon),
\]
since \(\sum_{j\ge0}(\sqrt{1+w_j^2}-1)\le\frac12\sum_{j\ge0}w_j^2<\infty\), and \(\varepsilon^2N_+=o(\varepsilon)\). The remaining segments and the central limit segment are contained in the rectangle \([s_{N_+},1-s_{N_+}]\times[0,1]\), of width \(q^{N_+}\le\varepsilon\). Its \(\varepsilon\)-neighborhood lies in an enclosing rectangle of width at most \(3\varepsilon\) and height \(1+2\varepsilon\), hence contributes \(O(\varepsilon)\). Thus
\[
\operatorname{area}((\Gamma_q)_\varepsilon)\le4\varepsilon N_+(\varepsilon)+O_q(\varepsilon).
\]

**4. Lower Euclidean neighborhood estimate.** Choose the largest positive integer \(N_-(\varepsilon)\) such that both \(w_{N_--1}>4\varepsilon\) and \(q^{N_-}>4\varepsilon\). At every height \(y\in[0,1]\), the \(2N_-\) graph abscissae \(P_j^L(y)_1,P_j^R(y)_1\), for \(j<N_-\), are pairwise more than \(4\varepsilon\) apart. For neighboring left branches the difference is \(w_j(1-y)+w_{j+1}y\ge w_{j+1}>4\varepsilon\); the right branches are symmetric. The innermost left/right separation is
\[
q^{N_--1}\bigl(1-(1-q)y\bigr)\ge q^{N_-}>4\varepsilon.
\]
Consequently the horizontal \(\varepsilon\)-intervals centered at these graph points are pairwise disjoint at every height, all lie within the Euclidean graph neighborhood, and have total length \(4\varepsilon N_-\). Integrating over \(0\le y\le1\) proves
\[
\operatorname{area}((\Gamma_q)_\varepsilon)\ge4\varepsilon N_-(\varepsilon).
\]
Both cutoffs satisfy \(N_\pm(\varepsilon)=\log(1/\varepsilon)/\log(1/q)+O_q(1)\) as \(\varepsilon\downarrow0\). The upper and lower estimates combine to give the stated coefficient and \(O_q(\varepsilon)\) remainder. The box dimension follows from the standard equivalence between the logarithmic volume decay of Euclidean neighborhoods and box-counting dimension for bounded subsets of \(\mathbb R^2\).

## Verification
A standalone script, `verify.py`, independently checks 1,276 exact-rational branch/inverse-cylinder identities for four rational parameter choices. It also computes horizontal \(\varepsilon\)-cross-section covering probes at three scales for each of two source-paper parameters and compares their scaled growth with the proved logarithmic coefficient. These finite checks support implementation accuracy; the proof of the all-parameter, all-scale assertion is the preceding analytical argument. Run with `python3 verify.py` using the Python standard library only.

## Relationship to prior work
Kopets, Rybin, Vasilchenko, Butusov, Fedoseev, and Karimov introduced this countable-branch map and estimated its graph box dimension numerically as \(1.24\) for \((d,q)=(1/3,1/3)\) and \(1.29\) for \((d,q)=(1/4,1/2)\). The exact geometric tube law here gives asymptotic dimension \(1\) at both points and throughout the balanced family. It identifies a logarithmic finite-resolution effect rather than assigning an unverified cause to the earlier numerical estimates. The full-branch symbolic-measure argument is a standard form of generalized Lüroth coding; no novelty is asserted for Bernoulli coding as a general method. Prior work by Kesseböhmer, Munday, and Stratmann studies exactness and Lyapunov spectra for broad generalized Lüroth families, but its theorems concern orbit behavior and multifractal spectra, not the Euclidean graph-tube area or its explicit logarithmic coefficient for this two-sided geometric construction. The novelty asserted here is the explicit combined exact description for the specified 2024 map, particularly its graph-tube asymptotic.

## Limitations
This theorem treats only the balance locus \(d=(1-q)/2\) with fixed \(0<q<1\), where all countable branches exactly cover both half intervals; it does not describe off-locus branch-search termination or finite-precision implementations. Lebesgue invariance and the entropy calculation hold modulo exceptional branch boundaries, whose values are not fixed by the source algorithm. The theorem does not establish cryptographic security or an appropriate topological entropy for a discontinuous map. The geometric asymptotic does not establish an error model for any particular finite-sampling box-counter. Generic graph-neighborhood results or as-yet-unlocated prior calculations could overlap with the explicit tube coefficient; comprehensive publication-priority confirmation and independent mathematical audit remain outstanding.

## References
1. E. Kopets, V. Rybin, O. Vasilchenko, D. Butusov, P. Fedoseev, and A. Karimov, “Fractal Tent Map with Application to Surrogate Testing,” *Fractal and Fractional* **8** (2024), 344, published June 7, 2024. DOI: 10.3390/fractalfract8060344.
2. M. Kesseböhmer, S. Munday, and B. O. Stratmann, “Strong renewal theorems and Lyapunov spectra for \(\alpha\)-Farey and \(\alpha\)-Lüroth systems,” *Ergodic Theory and Dynamical Systems* **32** (2012), 989–1017, arXiv:1006.5693.
3. H. Bruin and M. Todd, “Transience and thermodynamic formalism for infinitely branched interval maps,” *Journal of the London Mathematical Society* **86** (2012), 171–194. DOI: 10.1112/jlms/jdr081.
