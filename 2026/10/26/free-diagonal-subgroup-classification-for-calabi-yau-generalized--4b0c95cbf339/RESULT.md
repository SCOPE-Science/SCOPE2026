# Free diagonal subgroup classification for Calabi–Yau generalized Fermat manifolds

## Finding

Let \(k\geq2\) and \(t\geq1\) be integers, put \(N=kt\) and \(d=(k-1)t-1\geq2\), and let \(M\subset\mathbb P^{N-1}_{\mathbb C}\) be any smooth generalized Fermat manifold of Calabi–Yau type: a complete intersection of \(t\) diagonal equations of degree \(k\), with the coefficient hyperplanes in general position. Consider its distinguished diagonal projective group
\[
H=(\mu_k)^N/\mu_k\cong(\mathbb Z/k\mathbb Z)^{N-1},
\]
where the denominator is the diagonal scalar subgroup.

**Classification and count.** If \(k\) is composite, \(H\) has no nontrivial subgroup acting freely on \(M\). If \(k=p\) is prime, then a nontrivial subgroup \(G\leq H\) acts freely exactly when the following condition holds. Write \(G\cong(\mathbb F_p)^r\) with \(r\geq1\). After a linear lift to diagonal matrices, the \(N\) coordinate characters \(\chi_1,\ldots,\chi_N\in G^*=\operatorname{Hom}_{\mathbb F_p}(G,\mathbb F_p)\) must contain **every** character exactly
\[
m=\frac{N}{p^r}=\frac{t}{p^{r-1}}
\]
times. Equivalently, \(p^{r-1}\) divides \(t\). Conversely, every such balanced character array defines a free subgroup. The number of distinct rank-\(r\) free subgroups **inside the fixed, coordinate-labelled group** \(H\) is precisely
\[
\boxed{\mathcal N_{p,t}(r)=\frac{(pt)!}{p^r\,(m!)^{p^r}\prod_{i=0}^{r-1}(p^r-p^i)}}
\quad\text{if }p^{r-1}\mid t,
\]
and is zero otherwise. In particular, the maximum free diagonal subgroup rank is \(1+v_p(t)\). The count is of subgroups of \(H\), not of abstractly nonisomorphic quotient varieties and not modulo permutations of coordinate positions.

For \(p=3,t=3\), the smooth fivefold \(M\), a generalized Fermat complete intersection of three cubics in \(\mathbb P^8\), admits exactly \(840\) rank-two free subgroups \(G\cong(\mathbb Z/3\mathbb Z)^2\). Each quotient \(Y=M/G\) is smooth, has trivial canonical bundle,
\[
\pi_1(Y)\cong(\mathbb Z/3\mathbb Z)^2,\qquad \rho(Y)=1,\qquad \chi_{\mathrm{top}}(Y)=-1080.
\]
All three invariants concern the resulting free quotient, not a singular coarse quotient. For even-dimensional Calabi–Yau generalized Fermat manifolds, every nontrivial free subgroup of \(H\) is necessarily cyclic of order two.

## Assumptions and scope

Everything is over \(\mathbb C\), and the hyperplanes determining the generalized Fermat pair are in general position, so \(M\) is smooth and the fixed-point criterion below applies. The Calabi–Yau relation \(N=kt\), \(d=(k-1)t-1\) is essential. A "free subgroup" means that **every** nonidentity element has empty fixed locus on \(M\). Coordinate positions are labelled by the given embedding in projective space. No classification is asserted for subgroups of the full automorphism group outside \(H\), nor for isomorphism classes of quotients.

## Proof

**1. Geometric fixed-point criterion.** Write the exponent vector of a diagonal automorphism \(g\in H\) as \((a_1,\dots,a_N)\in(\mathbb Z/k\mathbb Z)^N\), defined modulo a constant vector. Proposition 3 of Hidalgo–Hughes–Leyton-Álvarez, or Proposition 3.4 of Billi–Palomino–Sarti, says that the fixed locus on \(M\) is nonempty exactly when some exponent occurs at least \(N-d=t+1\) times. Therefore a nonidentity \(g\) is fixed-point-free if and only if *every* exponent occurs at most \(t\) times. Since there are \(k\) residues and \(N=kt\) entries, this is equivalent to every residue occurring **exactly** \(t\) times. In particular such an element has order exactly \(k\).

**2. Composite exponents.** Suppose \(k\) is composite and \(G\leq H\) is a nontrivial free subgroup. Pick nonidentity \(g\in G\). By step 1 its order is \(k\); a proper nontrivial power \(g^a\) has order strictly between \(1\) and \(k\), and lies in \(G\). Step 1 implies \(g^a\) has a fixed point, a contradiction. Thus no such subgroup exists.

**3. Fourier rigidity for prime exponents.** Assume \(k=p\) prime. Every subgroup \(G\leq H\) is a vector space over \(\mathbb F_p\), of rank \(r\). The short exact sequence of vector spaces \(0\to\mathbb F_p\mathbf1\to\mathbb F_p^N\to H\to0\) splits upon restriction to \(G\). Choosing a splitting expresses each of the \(N\) coordinate exponents as a linear character \(\chi_j\in G^*\). Any two splittings differ by adding one common \(\lambda\in G^*\) to all \(\chi_j\).

Fix a primitive \(p\)-th root \(\zeta\). If \(G\) acts freely, step 1 applied to every \(g\in G\setminus\{0\}\) gives
\[
\sum_{j=1}^{N}\zeta^{\chi_j(g)}=t\sum_{a\in\mathbb F_p}\zeta^a=0.
\]
Let \(c(\chi)\) be the number of occurrences of \(\chi\in G^*\). Its Fourier transform on the finite abelian group \(G^*\) has value \(N\) at \(g=0\) and zero at each \(g\ne0\). Fourier inversion yields \(c(\chi)=N/p^r\) for every \(\chi\). Hence \(m=N/p^r\) is an integer and is equal to \(t/p^{r-1}\). Conversely, if all \(p^r\) characters occur \(m\) times, evaluation at every nonzero \(g\) takes each residue exactly \(mp^{r-1}=t\) times, since a nonzero linear functional on \(G^*\) has fibers of size \(p^{r-1}\). Thus the induced action is fixed-point-free and faithful. This proves the classification and the divisibility criterion.

**4. Enumeration and identifications.** For a fixed coordinate labelling, there are \(N!/(m!)^{p^r}\) ordered character arrays containing each of the \(p^r\) characters exactly \(m\) times. Translating all characters by any \(\lambda\in G^*\) changes only the splitting, not the subgroup of \(H\), and gives \(p^r\) distinct arrays. Changing the chosen basis of \(G\) acts by \(\mathrm{GL}_r(\mathbb F_p)\), of order \(\prod_{i=0}^{r-1}(p^r-p^i)\). These two actions together form the affine group on the character labels and act freely on balanced arrays: all characters occur, so an affine transformation fixing the array fixes every character and must be the identity. Conversely any two arrays defining the same embedded subgroup differ by a basis change and a splitting change. Dividing by this full affine-group order proves the stated exact count. The largest permitted rank is \(1+v_p(t)\).

**5. Fivefold consequence.** For \(p=t=3\), \(N=9\), \(r=2\), \(m=1\) and \(|\mathrm{GL}_2(\mathbb F_3)|=(9-1)(9-3)=48\), giving \(9!/(9\cdot48)=840\). For a concrete subgroup, index the nine coordinates by \((a,b)\in\mathbb F_3^2\) and let \(g=(u,v)\) multiply coordinate \((a,b)\) by \(\zeta^{ua+vb}\). Each nonzero \(g\) has eigenvalues \(1,\zeta,\zeta^2\) exactly three times, hence acts without fixed points. Smoothness of \(Y\) follows from the finite étale quotient. Lefschetz hyperplane theory makes the smooth complete intersection \(M\) simply connected for \(d=5\), so \(\pi_1(Y)=G\). The rational second cohomology of \(M\) is spanned by the hyperplane class and remains invariant, hence \(h^{1,1}(Y)=\rho(Y)=1\). Since \(d=5\) is odd and every nontrivial element acts freely, the holomorphic Lefschetz number \(1-\operatorname{Tr}(g\mid H^5(M,\mathcal O_M))\) is zero, and Serre duality then forces trivial action on \(H^0(M,K_M)\); thus \(G\) preserves the nowhere-vanishing holomorphic volume form and \(K_Y\) is trivial. Finally, using the tangent exact sequence for three cubics, the fifth Chern class coefficient is
\[
[h^5]\frac{(1+h)^9}{(1+3h)^3}=-360,
\]
so \(\chi_{\mathrm{top}}(M)=-360\cdot27=-9720\), and multiplicativity under the degree-nine covering gives \(\chi_{\mathrm{top}}(Y)=-1080\).

**6. Even-dimensional boundary.** For an even \(d=(k-1)t-1\), parity forces \(k\) even and \(t\) odd. Composite \(k\) is already ruled out, leaving \(k=2\). Since \(v_2(t)=0\), the maximum rank is one, so only order-two free subgroups occur.

## Verification

The standalone file `verify.py` enumerates every balanced character ordering at the two smallest complete-affine rank examples and independently counts orbits under the full affine label group. It finds \(840\) rank-two subgroups for \((p,t)=(3,3)\), \(30\) rank-three subgroups for \((p,t)=(2,4)\), and \(1\) rank-two subgroup in the minimal \((p,t)=(2,2)\) calculation (the last has \(d=1\) and is **not** part of the dimension-at-least-two claim). It also checks cyclic counts \(280\) for \((3,3)\), \(10\) for \((2,3)\), character balance, and the exact fivefold Euler number. Execute with `python3 verify.py`; successful output begins `VERIFY_OK`.

The finite checker is corroboration, not the reason the classification holds for arbitrary \(p,t,r\): that assertion is proved by finite Fourier inversion and affine-array orbit counting above.

## Relationship to prior work

Billi–Palomino–Sarti (2026), Proposition 4.1 and Section 4, classify individual fixed-point-free automorphisms in \(H\), their powers, and cyclic quotients; their Proposition 3.4 supplies the fixed-locus criterion. The new point here is the **simultaneous** condition for every nonidentity element of a subgroup and its exact Fourier-character classification, rank threshold, and count. Hidalgo–Hughes–Leyton-Álvarez (2020/2024), Proposition 3, establishes the general geometric fixed-point criterion and discusses constraints for some free subgroups, but its stated results do not evaluate the all-rank Calabi–Yau subgroup census. Hidalgo (2022), Proposition 4, classifies free subgroups of generalized Fermat *curves* through homomorphism kernels, not the higher-dimensional Calabi–Yau fixed-point condition. Hua (2010/2011) classifies free actions on complete intersections of *four quadrics in \(\mathbb P^7\)*, including an order-eight elementary abelian possibility: this covers a special threefold group type, but not the all-parameter diagonal character census or the three-cubic fivefold case. Counts here are labelled subgroup counts, not projective-equivalence class counts in Hua.

## Limitations

The theorem only concerns the distinguished diagonal group \(H\), not arbitrary projective or abstract automorphisms. It counts embedded subgroups, not distinct quotient isomorphism classes. The classification depends on smoothness and the Calabi–Yau numerical relation; no extension to other complete-intersection types is claimed. The source papers give key fixed-point and smoothness inputs; they are cited rather than reproved. An implicit earlier character-theoretic formulation, especially in broader finite-group-action literature, remains a residual priority risk. Independent mathematical validation has not been performed.

## References

1. S. Billi, A. J. Palomino, A. Sarti, *Quotients of Calabi–Yau Generalized Fermat manifolds and Log Enriques varieties*, arXiv:2610.21752v1, first posted 15 October 2026, especially Propositions 3.4, 3.6, 4.1, 4.7, 4.8. https://arxiv.org/pdf/2610.21752
2. R. A. Hidalgo, H. F. Hughes, M. Leyton-Álvarez, *Automorphisms of generalized Fermat manifolds*, arXiv:2010.04628, especially Proposition 3 and Remark 5. https://arxiv.org/pdf/2010.04628
3. R. A. Hidalgo, *Smooth quotients of generalized Fermat curves*, arXiv:2202.12663, especially Proposition 4 on the curve case. https://arxiv.org/pdf/2202.12663
4. Z. Hua, *Classification of free actions on complete intersections of four quadrics*, arXiv:0707.4339; Adv. Theor. Math. Phys. 15 (2011), 973–990, especially Section 5. https://arxiv.org/pdf/0707.4339
