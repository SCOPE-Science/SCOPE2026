# Sharp Hilbert distortion and alternating-simplex rigidity for even-rim wheels

## Finding

For every integer \(m\ge7\), let \(G_m=K_1\vee C_{2m}\) be the unweighted wheel formed by joining one hub \(o\) to all \(2m\) vertices of an even cycle. Give \(G_m\) its unit-edge shortest-path metric \(d\). Its least real Hilbert bi-Lipschitz distortion is exactly
\[
 c_2(G_m)=\sqrt{2-\frac2m}.
\]
Equivalently, the squared optimum for a noncontracting embedding is \(T_m=2-2/m\). In **every** optimum embedding scaled to satisfy \(d(u,v)\le\|f(u)-f(v)\|\), the \(m\) even-indexed rim vertices and, separately, the \(m\) odd-indexed rim vertices are regular Euclidean simplices of side length \(2\), each centered at the hub image and with squared circumradius \(T_m\). An explicit optimum embedding exists in real dimension \(2m-2\). The sharp constants strictly increase to \(\sqrt2\) as \(m\to\infty\).

## Assumptions and scope

Here \(C_{2m}\) has cyclically indexed vertices \(r_0,r_1,\ldots,r_{2m-1}\). All hub–rim and adjacent-rim distances are \(1\); all other distinct rim distances are \(2\). There are no edge weights, embedding-dimension bounds in the infimum, or symmetry requirements on competing embeddings. Distortion is the supremum of the distance ratios divided by their infimum, and an optimum can be rescaled to be noncontracting. Indices on the two parity classes below are taken modulo \(m\). The cutoff \(m\ge7\) is a proved sufficient range, not an assertion about every smaller wheel.

## Proof

**Universal lower bound and rigidity.** Fix any Hilbert embedding \(f\), rescaled to be noncontracting, and put \(x_i=f(r_{2i})-f(o)\). Distinct even rim vertices have graph distance \(2\), so \(\|x_i-x_j\|^2\ge4\). If the squared expansion bound is \(T\), then \(\|x_i\|^2\le T\). The Hilbert centroid identity gives
\[
 m\sum_i\|x_i\|^2-\Big\|\sum_i x_i\Big\|^2
 =\sum_{i<j}\|x_i-x_j\|^2\ge 4\binom m2.
\]
Thus \(m^2T\ge2m(m-1)\), or \(T\ge2-2/m\), with no assumption on the embedding dimension or symmetry. At equality, each inequality above is an equality: every hub–even distance squared is \(T_m\), every distinct even–even squared distance is \(4\), and the even vertices have centroid at the hub. Applying the same argument to the odd rim yields the two claimed regular simplices. This holds for **every** optimal embedding, not merely for the construction below.

**Explicit Gram construction.** Set \(T_m=2-2/m\). We prescribe a real symmetric \(2m\)-by-\(2m\) Gram matrix \(G\) for vectors \(e_i,o_j\), with hub at the origin. Within either parity class set
\[
 \langle e_i,e_j\rangle=\langle o_i,o_j\rangle=
 \begin{cases}T_m&i=j,\\-2/m&i\ne j.\end{cases}
\]
For the cross inner products put
\[
 \langle e_i,o_j\rangle=
 \begin{cases}
 1-1/m&j-i\equiv0,-1\pmod m,\\
 -3/m&j-i\equiv1,-2\pmod m,\\
 -2/m&\text{otherwise}.
 \end{cases}
\]
The three cases are disjoint for \(m\ge7\). Let \(J\) be the \(m\)-by-\(m\) all-ones matrix and let \(S\) be the cyclic shift with entries \(S_{ij}=1\) exactly when \(j-i\equiv1\pmod m\). In parity-block form,
\[
 G=\begin{pmatrix}H&C\\C^{\mathsf T}&H\end{pmatrix},\qquad
 H=2I-\frac2m J,\qquad
 C=(1+1/m)(I+S^{-1})-\frac1m(S+S^{-2})-\frac2m J.
\]
Both blocks kill constant vectors. On each nonconstant Fourier mode \(\theta=2\pi k/m\), \(1\le k\le m-1\), the two eigenvalues of \(G\) are \(2\pm|\lambda_k|\), with
\[
 |\lambda_k|=2u_k\left(1+\frac4m(1-u_k^2)\right),
 \qquad u_k=|\cos(\pi k/m)|<1.
\]
For \(m\ge8\), the function \(u\mapsto u(1+4(1-u^2)/m)\) increases on \([0,1]\), since its derivative is at least \(1-8/m\), and its value at \(1\) is \(1\). For \(m=7\), the discrete Fourier values satisfy \(u_k\le\cos(\pi/7)<91/100\): indeed \(\pi>3\) and the alternating Taylor bound give \(\cos(\pi/7)<\cos(3/7)\le17471/19208<91/100\). The same function is increasing on \([0,91/100]\) for \(m=7\), and its value at \(91/100\) equals \(249847/250000<1\). Therefore \(|\lambda_k|<2\) for all \(m\ge7\), and \(G\) is positive semidefinite, of rank \(2m-2\). Real Gram vectors \(e_i,o_j\) consequently exist in \(\mathbb R^{2m-2}\).

**Verification of all distances.** Hub–rim squared Euclidean distances are \(T_m\). Two distinct same-parity rim vertices have squared distance exactly \(4\). Adjacent opposite-parity rim vertices have squared distance exactly \(T_m\). The two other near-cross positions \(j-i\equiv1,-2\pmod m\) have squared Euclidean distance \(4+2/m\), and all remaining cross pairs have squared distance \(4\). Their graph distances are \(2\). Because \(m\ge7\),
\[
 4\le4+2/m\le4T_m,
\]
and \(1\le T_m\). Thus every pair obeys
\[
 d(u,v)^2\le\|f(u)-f(v)\|^2\le T_m d(u,v)^2.
\]
Some distance-two pairs attain the lower equality and each hub–rim pair attains the upper. Together with the universal lower bound this proves the theorem, including the stated rigidity and limit.

## Verification

The standalone pure-Python program `check_wheel.py` reconstructs the proposed Gram matrix with rational entries for every \(7\le m\le18\), proves its positive semidefiniteness via exact rational Schur complements, independently computes all wheel shortest-path distances, and verifies each proposed squared-distance inequality exactly. The observed result was `CHECK_OK exact_rational_PSD_and_pair_bounds=12 rim_orders=14..36 edges=600 nonedges=3586`. These finite checks are supplementary; the Fourier bound above proves positive semidefiniteness for every integer \(m\ge7\), not just the tested cases.

## Relationship to prior work

Balaji, Bapat, and Goel (arXiv:2006.03289, first publicly submitted 2020-06-05) examine exactly the same odd-order wheel family but derive a Moore–Penrose inverse and Euclidean-distance-matrix representation for the **unsquared** graph-distance matrix. That representation concerns isometric Hilbert realization of the square-root metric, which gives at most a \(\sqrt2\) distortion embedding for the original graph metric; it does **not** yield this sharp finite-size \(\sqrt{2-2/m}\) constant or the necessity of the two alternating simplices. Their full manuscript's setup, main theorem, and Euclidean-distance-matrix discussion were compared.

Vallentin (arXiv:math/0509716) and Cioabă–Gupta–Ihringer–Kurihara (arXiv:2109.09708) calculate or bound least Euclidean distortion for distance-regular families, including Johnson and strongly regular graphs; the nonregular wheels here are not a consequence of those formulae. Abraham–Filtser–Gupta–Neiman (arXiv:1708.04073) give asymptotic graph-family embedding bounds, not an exact wheel constant. Results on wheel symmetric-edge-polytope ellipsoids, wheel circulation projections, and the powered-metric negative-type threshold concern different Banach or metric invariants; none of their inspected statements implies this cotype-free, original-metric Euclidean distortion formula. Search non-detection is not a proof of global publication priority.

## Limitations

Only the even-rim wheels with \(m\ge7\) are covered. The theorem does not classify odd-rim wheels, the smaller even-rim cases, weighted edges, or minimal Hilbert dimension among all optimal embeddings. The explicit construction has dimension \(2m-2\), but lower dimension is not excluded. Historical novelty has not been independently certified. No claim is made about results on Mahler products or Banach–Mazur distortion of wheel Lipschitz-free spaces, which are different invariants.

## References

1. R. Balaji, R. B. Bapat, and S. Goel, *On distance matrices of wheel graphs with odd number of vertices*, arXiv:2006.03289, original submission 2020-06-05, https://arxiv.org/abs/2006.03289.
2. F. Vallentin, *Optimal distortion embeddings of distance regular graphs into Euclidean spaces*, arXiv:math/0509716, original submission 2005-09-30, https://arxiv.org/abs/math/0509716.
3. S. M. Cioabă, H. Gupta, F. Ihringer, and H. Kurihara, *The least Euclidean distortion constant of a distance-regular graph*, arXiv:2109.09708, original submission 2021-09-20, https://arxiv.org/abs/2109.09708.
4. I. Abraham, A. Filtser, A. Gupta, and O. Neiman, *Metric Embedding via Shortest Path Decompositions*, arXiv:1708.04073, original submission 2017-08-14, https://arxiv.org/abs/1708.04073.
