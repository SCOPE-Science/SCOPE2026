# Tri-colored sum-free sets characterize group-developed three-row perfect hash families

## Result

Let \(G\) be a finite abelian group of order \(q\ge 3\). Call a three-row array over alphabet \(G\) **diagonally \(G\)-developed** if its column set is invariant under simultaneous translation
\[
(a,b,c)\mapsto(a+g,b+g,c+g)\qquad(g\in G).
\]
The diagonal action is free, so every orbit contains a unique representative with first coordinate \(0\).

Let \(M_3(G)\) denote the maximum size of a tri-colored sum-free set in \(G\): a family
\[
T=\{(x_i,y_i,z_i):1\le i\le m\}\subseteq G^3
\]
with \(x_i+y_i+z_i=0\) for every \(i\), and
\[
x_i+y_j+z_k=0\quad\Longleftrightarrow\quad i=j=k.
\]
Then the maximum number of columns in a diagonally \(G\)-developed \(\operatorname{PHF}(3;k,q,3)\) is exactly
\[
\boxed{k=qM_3(G)}.
\]
More precisely, tri-colored sum-free sets of size \(m\) are in bijective correspondence, up to the choice of normalized orbit representatives, with diagonally \(G\)-developed three-row perfect hash families having \(qm\) columns.

Given \(T\), the corresponding columns are
\[
C(g,i)=\begin{pmatrix}g\\g+y_i\\g-x_i\end{pmatrix},
\qquad g\in G,\ 1\le i\le m.
\]
Conversely, if a developed family has normalized orbit representatives \((0,r_i,s_i)^T\), its tri-colored set is
\[
(x_i,y_i,z_i)=(-s_i,r_i,s_i-r_i).
\]

## Proof

First suppose \(T\) is tri-colored sum-free. Its three coordinate lists are injective. For example, if \(z_i=z_j\) with \(i\ne j\), then the diagonal identity \(x_i+y_i+z_i=0\) also gives the forbidden off-diagonal identity \(x_i+y_i+z_j=0\). The same argument applies to the \(x\)- and \(y\)-coordinates.

Consider two columns \(C(g,i)\) and \(C(h,j)\). If they agree in rows 1 and 2, then \(g=h\) and \(y_i=y_j\), hence \(i=j\) and the columns coincide. Agreement in rows 1 and 3 is identical. Agreement in rows 2 and 3 gives
\[
x_i+y_i=x_j+y_j,
\]
so \(z_i=z_j\), again forcing \(i=j\) and then \(g=h\). Thus two distinct columns collide in at most one row.

Assume three distinct columns are not separated by any row. Since no pair can collide twice, the three rows must realize the three different collision pairs. Relabeling the columns if necessary, write their indices and translations as \((i,g_1),(j,g_2),(k,g_3)\) and arrange
\[
 g_1=g_2,
\]
\[
 g_2+y_j=g_3+y_k,
\]
\[
 g_3-x_k=g_1-x_i.
\]
Eliminating the translations yields
\[
x_i+y_j+z_k=0.
\]
The tri-colored sum-free property gives \(i=j=k\). The first two displayed equalities then give \(g_1=g_2=g_3\), contradicting that the columns were distinct. Hence every three columns are separated in some row, so the array is a \(\operatorname{PHF}(3;qm,q,3)\).

For the converse, normalize each translation orbit of a diagonally developed PHF as \((0,r_i,s_i)^T\) and put
\[
(x_i,y_i,z_i)=(-s_i,r_i,s_i-r_i).
\]
Then \(x_i+y_i+z_i=0\). The PHF property together with translation closure forces each of the three coordinate lists \((x_i),(y_i),(z_i)\) to be injective. For instance, if \(y_i=y_j\) with \(i\ne j\), then the normalized columns for \(i,j\) collide in rows 1 and 2. If \(x_i\ne x_j\), translate the \(j\)-orbit by \(x_j-x_i\) to obtain a third distinct column colliding with the \(i\)-column in row 3; if \(x_i=x_j\), the two normalized columns are already identical in all rows. Either case contradicts perfect hashing. The arguments for repeated \(x\) or \(z\) are symmetric (for \(z\), first translate one normalized representative so that rows 2 and 3 collide).

Now suppose \(x_i+y_j+z_k=0\). If two of \(i,j,k\) are equal but not all three, comparison with the corresponding diagonal equation forces a repeated coordinate, contradicting the injectivity just established. If \(i,j,k\) are all distinct, take the three columns
\[
C(0,i),\qquad C(0,j),\qquad C(y_j-y_k,k).
\]
Rows 1, 2, and 3 respectively contain a collision in the pairs \((i,j)\), \((j,k)\), and \((k,i)\), where the row-3 equality is exactly the assumed equation. Hence the three columns would not be separated, contradicting the PHF property. Therefore only \(i=j=k\) is possible, and the normalized orbit data form a tri-colored sum-free set. This proves the correspondence and \(k=qM_3(G)\).

## Consequence: exact asymptotic capacity of the developed class

For a prime \(p\), set
\[
\theta_p=\min_{\rho>0}(1+\rho+\cdots+\rho^{p-1})\rho^{-(p-1)/3}.
\]
Blasiak, Church, Cohn, Grochow, Naslund, Sawin and Umans bounded tri-colored sum-free sets in \(\mathbb F_p^n\) by \(3\theta_p^n\), while Kleinberg, Sawin and Speyer proved matching exponential-order lower bounds: for every \(\delta>0\), sufficiently large \(n\) admit tri-colored sum-free sets of size at least \((\theta_p-\delta)^n\). Therefore, if \(D_p(n)\) is the largest number of columns in a diagonally \(\mathbb F_p^n\)-developed three-row PHF, then
\[
\boxed{D_p(n)=(p\theta_p)^{n+o(n)}}.
\]
Equivalently, for alphabet size \(q=p^n\),
\[
D_p(n)=q^{1+\log_p\theta_p+o(1)}.
\]
For \(p=3\), \(\theta_3\approx2.755104613\), so the exponent is approximately
\[
1+\log_3\theta_3\approx1.922486872.
\]
By contrast, unrestricted three-row perfect hash families satisfy \(p_3(3,q)=q^{2-o(1)}\) along general growing alphabets. Thus diagonal translation symmetry imposes a genuine polynomial-exponent loss in fixed characteristic: this natural developed subclass cannot attain the unrestricted near-quadratic scale.

## Concrete finite-field corollary

Kable, Mills and Wright proved in 2026 that the 20 nonzero fourth powers in \(\mathbb F_{81}\) form a cap set. In characteristic three, any cap \(A\subseteq\mathbb F_3^n\) gives the tri-colored sum-free set \(\{(a,a,a):a\in A\}\). Hence their 20-element cap gives
\[
\boxed{\operatorname{PHF}(3;1620,81,3)}
\]
with columns
\[
(g,g+a,g-a)^T,\qquad g\in\mathbb F_{81},\ a\in A.
\]
The attached verifier reconstructs \(\mathbb F_{81}=\mathbb F_3[x]/(x^4-x-1)\), takes the subgroup of fourth powers, verifies the cap condition, constructs all 1620 columns, confirms that no pair collides in two rows, and exhaustively checks the resulting collision graph has no bad three-column triangle.

This 1620-column specialization improves the \(v=81\) 1296-column entry explicitly reported by Walker and Colbourn (2007). It is not asserted to be the current global record for \(v=81\): the historical online PHF tables cited in later literature were not accessible in the present literature check, and later constructions may contain stronger isolated parameters.

## Relation to prior work

Walker and Colbourn used three-term-progression-free subsets of \(\mathbb Z_v\) to construct three-row PHFs. Their construction is recovered here by the special tri-colored seed
\[
(-a_i,-a_i,2a_i),
\]
for which the tri-colored condition reduces to the absence of nontrivial three-term progressions. Thus the theorem upgrades the one-colored progression-free seed to the full tri-colored additive-matching object and identifies the exact structured capacity of all diagonal-translation-developed families.

Shangguan and Ge later connected PHFs to additive and hypergraph extremal problems and proved \(q^{2-o(1)}<p_3(3,q)=o(q^2)\); the 2025 work of Wei, Zhang and Ge extends the near-quadratic lower/upper scale to \(p_t(t,q)\) for all fixed \(t\ge3\). Their displayed constructions use one-dimensional solution-free seeds of the form \((y+b_1m,\ldots,y+b_tm)\). The present correspondence concerns a different natural symmetry class: arbitrary unions of full diagonal translation orbits in three coordinates, whose exact seed object is a tri-colored sum-free set.

## Limitations

- The exact correspondence is for three rows and strength three. It does not directly generalize to arbitrary \(t\) without replacing tri-colored sum-freeness by a higher-dimensional condition.
- The asymptotic obstruction applies to the diagonally developed subclass, not to unrestricted PHFs.
- The finite \(v=81\) corollary is compared only with explicitly inspected published constructions; no claim of a present-day global record is made.
- Originality is to the best of our knowledge. The most relevant residual risk is that the correspondence may appear implicitly under a different language such as group-developed triple systems, induced matchings, or additive hypergraphs.

## References

1. R. A. Walker II and C. J. Colbourn, “Perfect Hash Families: Constructions and Existence,” *Journal of Mathematical Cryptology* 1(2), 125–150 (2007). https://doi.org/10.1515/JMC.2007.008
2. R. Fuji-Hara, “Perfect hash families of strength three with three rows from varieties on finite projective geometries,” *Designs, Codes and Cryptography* 77, 351–356 (2015). https://doi.org/10.1007/s10623-015-0052-z
3. C. Shangguan and G. Ge, “Separating Hash Families: A Johnson-type bound and New Constructions,” *SIAM Journal on Discrete Mathematics* 30(4), 2243–2264 (2016). https://doi.org/10.1137/15M103827X
4. J. Blasiak, T. Church, H. Cohn, J. A. Grochow, E. Naslund, W. F. Sawin and C. Umans, “On cap sets and the group-theoretic approach to matrix multiplication,” *Discrete Analysis* 2017:3 (2017). https://doi.org/10.19086/da.1245
5. R. Kleinberg, W. Sawin and D. Speyer, “The Growth Rate of Tri-Colored Sum-Free Sets,” *Discrete Analysis* 2018:12 (2018). https://doi.org/10.19086/da.3734
6. X. Wei, X. Zhang and G. Ge, “Separating hash families with large universe,” *Journal of Combinatorial Theory, Series A* 216, 106075 (2025). https://doi.org/10.1016/j.jcta.2025.106075
7. A. Kable, M. Mills and D. J. Wright, “Subgroups of Finite Fields As Cap Sets,” arXiv:2604.26989 (2026). https://arxiv.org/abs/2604.26989
