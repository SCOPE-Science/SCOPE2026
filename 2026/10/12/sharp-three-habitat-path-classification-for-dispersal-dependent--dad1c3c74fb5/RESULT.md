# Sharp three-habitat path classification for dispersal-dependent growth rankings

## Finding
Consider three habitat patches joined as a path, with symmetric nearest-neighbor movement at common rate \(d>0\). Three distinct positive local per-capita net growth rates are \(h>m>\ell>0\). For a rate ordering \(r=(r_1,r_2,r_3)\), let \(\lambda_r(d)\) be the largest eigenvalue of \(H_r(d)=\operatorname{diag}(r)-dL\), where \(L\) is the graph Laplacian of the three-vertex path. This eigenvalue is the asymptotic exponential growth exponent of every initially positive population in the linear system.

Up to reversal of the path, the three layouts are \(R_m=(\ell,m,h)\), \(R_\ell=(m,\ell,h)\), and \(R_h=(m,h,\ell)\), with the subscript naming the center rate. For **every** \(d>0\), \(\lambda_{R_m}(d)\) is strictly larger than both competitors. The other two layouts have the following complete ranking:

- If \(2m\le h+\ell\), then \(\lambda_{R_\ell}(d)>\lambda_{R_h}(d)\) for every finite \(d>0\).
- If \(2m>h+\ell\), put
\[
d_*=\frac{(h-m)(m-\ell)}{2m-h-\ell}>0.
\]
Then \(\lambda_{R_\ell}(d)>\lambda_{R_h}(d)\) for \(0<d<d_*\), the exponents are equal **only** at \(d=d_*\), and \(\lambda_{R_\ell}(d)<\lambda_{R_h}(d)\) for \(d>d_*\). The crossing is transverse. At that crossing the common largest eigenvalue is exactly \(m\).

Among connected, unweighted, undirected habitat networks, three vertices are the smallest possible order for a strict reversal of the ranking of growth-rate permutations as uniform dispersal varies. The path gives the example; one- and two-vertex connected networks and the three-vertex triangle cannot have such a reversal.

For example, \((h,m,\ell)=(6,5,1)\) yields \(d_*=4/3\). Holding one endpoint's rate at \(5\), the alternative layouts \((5,1,6)\) and \((5,6,1)\) switch their growth ranking at that exact dispersal rate.

## Assumptions and scope
The habitat graph is the undirected path with two unit-weight edges connecting vertices 1–2 and 2–3. The Laplacian is
\[
L=\begin{pmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{pmatrix}.
\]
Population abundances \(u_i(t)\) follow \(\dot u(t)=H_r(d)u(t)\). Dispersal conserves total population, local growth is linear, the three rates are distinct and positive, and \(d\) is finite and strictly positive. The ordering statements compare distinct placements of one fixed multiset of rates; the equality at \(d=0\) and common limit \((h+m+\ell)/3\) as \(d\to\infty\) are not positive-dispersal ranking reversals. The single-species linear exponent is not a global conclusion about nonlinear competition or persistence under demographic noise.

## Proof
**1. Perron and limiting facts.** For \(d>0\), the matrix \(H_r(d)\) is symmetric and irreducible Metzler, hence its largest eigenvalue \(\lambda_r(d)\) is simple with a strictly positive normalized eigenvector \(v(d)\). The Rayleigh formula and differentiation give
\[
\lambda_r'(d)=-v(d)^\top Lv(d)=-\sum_{\{i,j\}\in E(P_3)}(v_i(d)-v_j(d))^2<0.
\]
Equality would force \(v\) constant and then all three local rates equal, contrary to the hypothesis. Comparing with the constant vector in the Rayleigh quotient shows \(\lambda_r(d)>(h+m+\ell)/3\). Since \(-dL\) is negative semidefinite and the rates are distinct, \(\lambda_r(d)<h\); both inequalities are strict for finite \(d>0\). It follows from the same variational characterization, or from separation of the constant and orthogonal Laplacian modes, that \(\lambda_r(d)\downarrow(h+m+\ell)/3\) as \(d\to\infty\), while \(\lambda_r(d)\to h\) as \(d\downarrow0\).

**2. Exact comparison lemma.** Write \(F_{a,b,c}(z,d)=\det(zI-H_{(a,b,c)}(d))\). Direct expansion of the tridiagonal determinant gives the two identities
\[
F_{a,b,c}(z,d)-F_{a,c,b}(z,d)=d(z-a)(b-c),
\]
\[
F_{a,b,c}(a,d)=d\bigl[(a-b)(a-c)+d(2a-b-c)\bigr].
\]
Thus, for \(d>0\) and \(b\ne c\), two layouts with the same first-end growth rate and their other two rates swapped can share a largest eigenvalue only if that eigenvalue equals the common endpoint rate \(a\).

**3. The best layout.** At sufficiently small \(d>0\), elementary nondegenerate eigenvalue perturbation around the unique maximum \(h\) gives \(\lambda_r(d)=h-\deg(v_h)d+O(d^2)\), where \(v_h\) is the vertex carrying \(h\). Therefore putting \(h\) at an endpoint beats putting it at the center. If \(h\) is at an endpoint with adjacent growth rate \(q\), the refinement is
\[
\lambda_r(d)=h-d+\frac{d^2}{h-q}+O(d^3).
\]
The endpoint layout adjacent to \(m\) therefore beats the endpoint layout adjacent to \(\ell\) for small \(d\).

For the two endpoint-high layouts, reflect the path so that the shared first end has rate \(h\). The comparison lemma says any tie would have largest eigenvalue \(h\), excluded by step 1. For the medium-center versus high-center layouts, reflect so their shared first end has rate \(\ell\); a tie would have largest eigenvalue \(\ell\), also excluded by step 1. Since eigenvalues depend continuously on \(d\), the small-d orderings persist for all \(d>0\). Hence \(R_m\) is always uniquely optimal, while both remaining layouts are strictly worse.

**4. The sharp reversal.** The remaining pair \(R_\ell=(m,\ell,h)\) and \(R_h=(m,h,\ell)\) has the common first-end rate \(m\). By step 2, its principal exponents can coincide only at \(m\), and the second identity reduces to
\[
F_{m,\ell,h}(m,d)=F_{m,h,\ell}(m,d)
=d\bigl[-(h-m)(m-\ell)+d(2m-h-\ell)\bigr].
\]
If \(2m\le h+\ell\), this cannot vanish for \(d>0\), so continuity and the small-d ordering prove the first case. If \(2m>h+\ell\), it vanishes at the unique \(d_*\) displayed in the finding. Because \(m>(h+m+\ell)/3\) exactly in this regime, the strict decrease in step 1 implies that \(m\) is attained once by each largest-eigenvalue branch. A second eigenvalue cannot reach \(m\) for positive \(d\): the second eigenvalue is nonincreasing under subtraction of the positive semidefinite matrix \(dL\), begins at \(m\), and initially decreases strictly. Thus the shared root at \(d_*\) is indeed the Perron eigenvalue.

To establish a genuine sign change rather than a tangency, let \(Q(d)=F_{m,\ell,h}(m,d)=F_{m,h,\ell}(m,d)\). At \(d_*\), \(Q'(d_*)=d_*(2m-h-\ell)>0\). At a simple largest root of a real symmetric three-by-three characteristic polynomial, \(\partial_zF(m,d_*)>0\). The first determinant identity yields
\[
\partial_zF_{m,\ell,h}(m,d_*)-\partial_zF_{m,h,\ell}(m,d_*)=d_*(\ell-h)<0.
\]
Implicit differentiation at \(\lambda=m\) therefore gives \(\lambda_{R_\ell}'(d_*)<\lambda_{R_h}'(d_*)\). Together with uniqueness of the possible tie and the small-d ordering, this proves the asserted transverse reversal and the whole interval classification.

**5. Minimal order.** For one or two vertices, every permutation of local rates is implemented by a graph automorphism, so the growth matrices are permutation-similar for every \(d\). On three vertices, the only connected simple graphs are the path and triangle. The triangle also realizes all permutations by automorphisms; the path has the strict crossing constructed above. This proves minimality.

## Verification
The independent algebraic identities in step 2 and the rational witness are checked by the attached standalone script `verify.py` (Python 3 with SymPy). Run `python3 verify.py`. It verifies the characteristic identities symbolically for general real parameters, confirms the witness's six labeled rate permutations, isolates all three real characteristic roots in exact rational intervals at \(d=1\) and \(d=2\), and checks the unique exact crossing at \(d=4/3\). The all-parameter classification and minimal order follow from the preceding proof, not from finite computation.

## Relationship to prior work
Gourley and Kuang (2005) motivated dispersal–growth interactions by comparing where competitors place their reproduction rates, including a discrete model on a symmetric three-patch all-to-all network. Such a network is invariant under all rate permutations and does not yield the present path-dependent classification. Flather and Bevers (2002) studied habitat amount versus arrangement in a different, nonlinear discrete reaction–diffusion simulation; its habitat-arrangement effects motivate the question without supplying the present eigenvalue ranking theorem. Lin and coauthors (2014) studied nonlinear competition and diffusion in two patches. Nadin (2016) studied resource rearrangements and spreading in a continuous periodic model. These works establish the broader motivation and are not claimed as new. A potentially stronger graph-Schrödinger rearrangement theorem could imply some of these rankings; an exhaustive exclusion of such an implication is not asserted.

## Limitations
The crossover reverses the ranking of **two nonoptimal layouts**; the medium-center layout remains strictly best among all unconstrained placements for every positive rate. A practical choice between the crossing layouts therefore requires a real placement constraint, such as an endpoint whose intermediate growth rate is fixed. The theorem covers three distinct positive rates, uniform conservative symmetric dispersal on the unweighted three-vertex path, and linearized single-species growth only. It does not classify larger networks, asymmetric migrations, repeated rates, nonlinear coexistence, or stochastic survival probabilities. The literature comparison is not a proof of publication novelty.

## References
1. Gourley, S. A., and Kuang, Y. (2005). *Two-Species Competition with High Dispersal: The Winning Strategy*. Mathematical Biosciences and Engineering 2, 345–362. DOI: 10.3934/mbe.2005.2.345. Publisher records publication on 2005-03-01.
2. Flather, C. H., and Bevers, M. (2002). *Patchy Reaction-Diffusion and Population Abundance: The Relative Importance of Habitat Amount and Arrangement*. The American Naturalist 159, 40–56. DOI: 10.1086/324120.
3. Lin, K.-H., Lou, Y., Shih, C.-W., and Tsai, T.-H. (2014). *Global dynamics for two-species competition in patchy environment*. Mathematical Biosciences and Engineering 11, 947–970. DOI: 10.3934/mbe.2014.11.947.
4. Nadin, G. (2016). *The Effect of the Schwarz Rearrangement on the Periodic Principal Eigenvalue of a Nonsymmetric Operator*. arXiv:1609.01442v1.
5. Slavík, A. (2019). *Lotka–Volterra Competition Model on Graphs*. SIAM Journal on Applied Dynamical Systems. DOI: 10.1137/19M1276285. Only the available publisher abstract was checked for this comparison.
