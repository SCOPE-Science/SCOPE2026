# Three-divisibility and exact dyadic orbit census in cubic anti-conformist opinion networks

## Finding
Let \(n\ge3\), let \(G_n=C_n\square K_2\) be the connected simple cubic prism on \(2n\) vertices, and give each vertex a binary opinion. Update all opinions synchronously by the following conforming/non-conformist rule: an agent follows its three neighbors when they agree unanimously, and follows the **minority** opinion when its neighbors split two-to-one. Denote the global update by \(T_n\). The following three statements hold.

1. **A sharp reversibility criterion.** \(T_n\) is a permutation of the entire \(2^{2n}\)-configuration space if and only if \(3\nmid n\).
2. **Exact periodic core and transient depth.** If \(3\mid n\), put \(t=2^{\nu_2(n)}\), the largest power of two dividing \(n\). Exactly \(2^{2n-4t}\) configurations are periodic. Every trajectory enters a cycle within \(\tau=\max\{2,t\}\) updates, and this worst-case entry time is attained by some configurations.
3. **A full census on dyadic prisms.** If \(n=2^k\) with \(k\ge2\), every configuration is periodic, and the largest attainable least period is exactly \(2^{k-1}=n/2\). All least periods are powers of two. Define \(F_j=\#\operatorname{Fix}(T_n^{2^j})\). For \(0\le j\le k-1\),
   \[
   F_0=16,\qquad
   F_j=2^{2\min\{n,2^{j+1}\}}\quad(1\le j\le k-1).
   \]
   Consequently the number of distinct cycles of least length \(2^j\) is \((F_j-F_{j-1})/2^j\), where \(F_{-1}=0\). No other cycles occur. On \(G_8\), for example, there are exactly \(16\) fixed points, \(120\) two-cycles and \(16{,}320\) four-cycles.

The reversible/nonreversible dichotomy and the dyadic orbit census are aspects of one exact arithmetic classification of the same synchronous opinion rule on the same graph family. In particular, cubic anti-conformist networks of unbounded size admit cycles of unbounded length even though typical short cycles are observed on sampled random regular graphs.

## Assumptions and scope
The vertices are \((i,a)\in\mathbb Z/n\mathbb Z\times\{0,1\}\), with undirected edges from \((i,a)\) to \((i-1,a)\), \((i+1,a)\) and \((i,1-a)\). No loops, parallel edges, asynchronous updates, stochasticity, self-input or external influence are permitted. The three-input local rule has outputs \(0,1,0,1\) for respective counts \(0,1,2,3\) of opinion-one neighbors. All arithmetic on configurations is over \(\mathbb F_2\). An orbit is periodic when it is periodic from its initial state, not just eventually periodic. Transient entry time is the least nonnegative number of steps before reaching a periodic state.

This is the degree-three, weak-agreement threshold-one anti-conformist rule in the terminology of Behrens, Hudcová and Zdeborová. Its output equals the XOR of the three neighboring opinions. For the dyadic census, \(k\ge2\) ensures the ordinary cycle graph is simple.

## Proof
**1. Linearization and two-layer Jordan form.** Let \(R=\mathbb F_2[z]/(z^n-1)\), so that cyclic shift is multiplication by \(z\) and \(z^{-1}\) exists. Represent the two rows of opinions as \(u,v\in R\), let \(P=z+z^{-1}\), and let \(f=1+P\). Counting the three neighboring opinions modulo two gives
\[
T_n(u,v)=(Pu+v,\,Pv+u).
\]
With the invertible change of coordinates \(w=u+v\), the same update becomes
\[
(u,w)\longmapsto(fu+w,\,fw),\qquad
J=\begin{pmatrix}f&1\\0&f\end{pmatrix}.
\]
It follows that \(T_n\) is bijective precisely when \(f\) is invertible in \(R\). Since \(zf=z^2+z+1=:q(z)\), its invertibility is equivalent to \(\gcd(q(z),z^n-1)=1\). The irreducible polynomial \(q\) has roots of multiplicative order three in \(\mathbb F_4\), so this holds exactly when \(3\nmid n\). This proves the first statement.

**2. The periodic core when three divides the circumference.** Assume \(3\mid n\), write \(n=2^s m\) for odd \(m\), and set \(t=2^s\). Since \(q\mid z^m-1\) and \(m\) is odd, \(q\) occurs with multiplicity one in \(z^m-1\). The characteristic-two identity \(z^n-1=(z^m-1)^t\) shows that its multiplicity in \(z^n-1\) is exactly \(t\). The Chinese remainder theorem gives a decomposition of \(R\) into the \(q\)-primary factor \(R_q=\mathbb F_2[z]/(q^t)\), of binary dimension \(2t\), and a complementary factor \(R_\mathrm{inv}\), of binary dimension \(n-2t\). The element \(f=q/z\) is nilpotent of exact index \(t\) on \(R_q\) and invertible on \(R_\mathrm{inv}\).

On the two-copy primary factor, the displayed matrix satisfies for every positive integer \(r\)
\[
J^r=\begin{pmatrix}f^r&(r\bmod2)f^{r-1}\\0&f^r\end{pmatrix}.
\]
If \(t\ge2\), then \(t\) is even, \(J^t=0\), and \(J^{t-1}\ne0\) because its diagonal contains \(f^{t-1}\). If \(t=1\), then \(J\ne0\) but \(J^2=0\). Thus the nilpotency index is exactly \(\tau=\max\{2,t\}\). On the complementary two-copy factor, \(J\) is invertible; since it acts on a finite set, every state in that factor is periodic. A nilpotent transformation has no periodic vector other than zero. Therefore the complete periodic subspace has dimension \(2(n-2t)=2n-4t\), and precisely \(2^{2n-4t}\) elements. Every state reaches it after at most \(\tau\) steps, and the nonvanishing of the penultimate primary power shows that the bound is sharp.

**3. Dyadic fixed spaces and actual orbit lengths.** Suppose \(n=2^k\), \(k\ge2\). Write the original two-row map as \(M=\begin{psmallmatrix}P&1\\1&P\end{psmallmatrix}\). In characteristic two, its square is the diagonal block matrix with both blocks \(1+P^2\); consequently, for \(j\ge1\),
\[
M^{2^j}=\operatorname{diag}(1+P^{2^j},1+P^{2^j}),
\qquad P^{2^j}=z^{2^j}+z^{-2^j}.
\]
A row vector is therefore fixed by this iterate exactly when it is invariant under cyclic shift by \(2^{j+1}\), since \(z^{2^j}+z^{-2^j}=z^{-2^j}(z^{2^{j+1}}+1)\). Such rows have \(\gcd(n,2^{j+1})=\min(n,2^{j+1})\) independent bits; counting both layers gives the claimed \(F_j\) for \(j\ge1\).

For the first iterate, the equations \(M(u,v)=(u,v)\) give \(v=fu\) and \(u=fv=f^2u\). Since \(f^2=1+P^2\), this is \(P^2u=0\), equivalently invariance under shift by four. There are exactly \(\gcd(n,4)=4\) free bits, so \(F_0=2^4=16\).

At \(j=k-1\), the shift \(2^{j+1}=n\) is the identity and \(M^{n/2}=I\); thus all states are periodic with periods dividing \(n/2\). The preceding iterate has a strictly smaller fixed space (for \(k=2\), use \(F_0<2^{2n}\)); hence an orbit of length exactly \(n/2\) exists. Because every divisor of \(n/2\) is a power of two, the fixed-point differences count all primitive periods, each cycle being counted by the number of its states. This proves the final statement.

## Verification
Run `python3 verify.py` using the standard Python library. It constructs the actual \(2n\)-by-\(2n\) Boolean adjacency maps, calculates exact Gaussian-elimination ranks and matrix powers, and checks reversibility, periodic-core dimension and maximal transient depth for each \(3\le n\le36\). For \(n=4,8,16,32,64\), it checks the full dyadic fixed-space formula and operator order by exact binary linear algebra. It additionally exhausts every one of the \(256\) states for \(n=4\) and every one of the \(65{,}536\) states for \(n=8\), confirming the exact primitive-period counts. This finite verification does not replace the unrestricted polynomial-ring proof.

## Relationship to prior work
Behrens, Hudcová and Zdeborová (2023), Sections II–III and the discussion of short attractors, define conforming/non-conformist graph cellular automata and report numerical predominance of short attractors on randomly sampled regular graphs. Their paper describes the degree-five anti-conformist rule and does not classify the cubic prism's arithmetic reversibility, transient-core sizes or all-state dyadic cycle counts. Their conjectural **typical** short-cycle statement on random regular graphs is not contradicted: prisms form a highly structured deterministic family.

Marr and Hütt (2008) provide the general outer-totalistic graph-automaton formalism and empirical topology dependence, not the present binary cycle enumeration. Classical additive cellular automata (including Rule 150) and general finite-field linear-dynamical-system theory provide the underlying algebraic techniques; the reduction to a single circular Rule 150 is insufficient by itself to count the **entire two-layer prism state space**, including the non-symmetric states and the nonreversible three-divisibility branch. Published exact parity-network results for complete multipartite graphs and Hamming distance-two cube graphs address different graph families: their bounded periods do not cover the arbitrarily long dyadic-prism cycles.

## Limitations
The conclusions concern one specified parity-equivalent anti-conformist rule on cubic prisms, not all conforming/non-conformist rules or typical random-regular networks. The precise cycle census is claimed for dyadic circumferences, not all \(3\nmid n\). For other invertible circumferences the period lengths may involve factors other than two. An earlier equivalent theorem formulated in the language of linear cellular automata or graph-adjacency modules cannot be excluded from the presently inspected literature. The result receives no independent audit or validation here.

## References
1. F. Behrens, B. Hudcová and L. Zdeborová, *Dynamical Phase Transitions in Graph Cellular Automata*, arXiv:2310.15894v1, first public posting 2023-10-24, Sections II–III, VI and Appendix B. https://arxiv.org/abs/2310.15894
2. C. Marr and M.-T. Hütt, *Outer-totalistic cellular automata on graphs*, arXiv:0812.2408v1, first public posting 2008-12-12. https://arxiv.org/abs/0812.2408
3. *A mod-four orbit census for parity automata on distance-two Boolean cubes*, publicly available result, 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-mod-four-orbit-census-for-parity-automata-on-distance-two-bool--f288ef2fe8b4
4. *Sharp period-four census for complete multipartite parity automata*, publicly available result, 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-period-four-census-for-complete-multipartite-parity-automa--acea41c73be7
5. R. A. Hernández-Toledo, *Linear finite dynamical systems*, Communications in Algebra 33 (2005), 2977–2989. (Background framework; full text not inspected.)
