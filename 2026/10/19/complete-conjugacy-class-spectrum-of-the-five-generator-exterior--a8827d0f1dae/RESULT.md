# Complete conjugacy-class spectrum of the five-generator exterior-algebra unit group

## Finding
Let \(V\) be a five-dimensional vector space over \(\mathbb F_q\), let \(E=\bigwedge_{\mathbb F_q}V\), and let \(J=\bigoplus_{j=1}^{5}\bigwedge^jV\) be its augmentation ideal. Write \(G_q=1+J\). For every integer \(r\geq0\), let \(k_r(q)\) be the number of **ordinary** conjugacy classes of \(G_q\) whose size is exactly \(q^r\). Define \(K_q(T)=\sum_{r\geq0}k_r(q)T^r\).

For every odd prime power \(q\),
\[
\boxed{K_q(T)=q^{16}
+q^{14}(q-1){5\brack2}_qT^2
+q^{14}(q-1)(q^3-1){5\brack1}_qT^4
+q^{18}(q^5-1)T^8,}
\]
where \({5\brack j}_q\) denotes the Gaussian binomial coefficient counting \(j\)-subspaces of \(\mathbb F_q^5\). The only class sizes are \(1,q^2,q^4,q^8\): in particular no class of size \(q^6\) exists. The center has order \(q^{16}\), the group has order \(q^{31}\), and it has nilpotency class exactly two.

For every even prime power \(q\), the algebra \(E\) and group \(G_q\) are commutative, and \(K_q(T)=q^{31}\). The full unit group \(E^\times\cong\mathbb F_q^\times\times G_q\) has the same possible class sizes, with every coefficient of \(K_q\) multiplied by \(q-1\).

## Assumptions and scope
The exterior algebra here has the alternating convention \(v\wedge v=0\), also in characteristic two. Its standard squarefree-monomial basis gives \(\dim E=32\) and \(\dim J=31\). The odd augmentation subspace
\[
O=\bigwedge^1V\oplus\bigwedge^3V\oplus\bigwedge^5V
\]
has dimension \(16\); the positive even subspace
\[
P=\bigwedge^2V\oplus\bigwedge^4V
\]
has dimension \(15\). Thus \(J=P\oplus O\). All class counts are for conjugation within the indicated finite group and use the actual finite-field cardinality \(q\), not the characteristic prime alone.

The five-generator case is the first odd generator number for which the alternating form associated with the degree-three part can have two distinct nonzero ranks. That rank separation motivates this precise finite-dimensional unit-group calculation.

## Proof
**1. Centralizers reduce to exterior multiplication.** In odd characteristic, the even subspace \(P\) is central in \(E\), and any two odd elements anticommute. Therefore for \(a,b\in J\), with odd parts \(a_O,b_O\),
\[
ab-ba=2a_O\wedge b_O.
\]
Since every \(1+a\) with \(a\in J\) is invertible, \(1+b\) centralizes \(1+a\) if and only if \(a_O\wedge b_O=0\). Define the linear map \(L_a:O\to P\) by \(L_a(b)=a_O\wedge b\), and write \(r(a)=\operatorname{rank}L_a\). The \(15\) even coordinates of \(b\) are free and its \(16\) odd coordinates satisfy \(r(a)\) independent equations, so
\[
|C_{G_q}(1+a)|=q^{31-r(a)},\qquad |(1+a)^{G_q}|=q^{r(a)}.
\]
The rank is unchanged by varying the even part of \(a\).

**2. The rank with a nonzero linear component.** Suppose \(a_O=v+\alpha+\beta\), with \(v\in V\setminus\{0\}\), \(\alpha\in\bigwedge^3V\), and \(\beta\in\bigwedge^5V\). After a linear change of basis we may assume \(v=e_1\). Sending \(e_1\) to \(a_O\) and fixing the remaining generators extends to an automorphism of the exterior algebra: the new elements remain odd, anticommute and square to zero, and their linear parts form a basis, so the induced filtered-algebra endomorphism is invertible. It preserves parity. Thus \(L_a\) has the same rank as exterior multiplication by \(e_1\) on \(O\). Its component \(\bigwedge^1V\to\bigwedge^2V\) has rank \(4\), its component \(\bigwedge^3V\to\bigwedge^4V\) has rank \(\binom43=4\), and the degree-five component maps to zero. Hence
\[
r(a)=8\quad\text{whenever }v\ne0.
\]
There are \((q^5-1)q^{11}\) odd parts with this property, because \(\alpha\) and \(\beta\) are arbitrary.

**3. The rank with zero linear component.** If \(v=0\), then \(a_O=\alpha+\beta\) and the only potentially nonzero part of \(L_a\) is \(V\to\bigwedge^4V\), sending \(w\) to \(\alpha\wedge w\). Fix a volume identification \(\bigwedge^5V\cong\mathbb F_q\). The perfect wedge pairing identifies \(\alpha\in\bigwedge^3V\) with an alternating bilinear form
\[
B_\alpha(u,w)=\operatorname{vol}(\alpha\wedge u\wedge w)
\]
on \(V\). Under \(\bigwedge^4V\cong V^*\), the map \(w\mapsto\alpha\wedge w\) has exactly the rank of \(B_\alpha\). An alternating form in dimension five over odd characteristic has rank \(0,2\), or \(4\), and every such rank occurs.

A rank-two form has a three-dimensional radical. Choosing it and then a nondegenerate alternating form on the two-dimensional quotient yields
\[
N_2(q)={5\brack3}_q(q-1)={5\brack2}_q(q-1).
\]
A rank-four form has a one-dimensional radical. A nondegenerate alternating form on a four-dimensional quotient is an \(\mathrm{GL}_4(\mathbb F_q)\)-translate of the standard symplectic form, with stabilizer \(\mathrm{Sp}_4(\mathbb F_q)\). Consequently,
\[
N_4(q)={5\brack1}_q\frac{|\mathrm{GL}_4(\mathbb F_q)|}{|\mathrm{Sp}_4(\mathbb F_q)|}
={5\brack1}_qq^2(q-1)(q^3-1).
\]
There is one rank-zero form. These counts satisfy \(1+N_2(q)+N_4(q)=q^{10}\), as they must since \(\dim\bigwedge^3V=10\). The degree-five coefficient \(\beta\) remains arbitrary and does not affect rank.

**4. Class-size polynomial.** For each odd part of rank \(r\), the even part has \(q^{15}\) choices. The number of elements of each rank, and the number of corresponding conjugacy classes, are therefore
\[
\begin{array}{c|c|c}
r&\text{elements}&k_r(q)\\\hline
0&q^{16}&q^{16}\\
2&q^{16}N_2(q)&q^{14}N_2(q)\\
4&q^{16}N_4(q)&q^{12}N_4(q)\\
8&q^{26}(q^5-1)&q^{18}(q^5-1).
\end{array}
\]
This is precisely the displayed polynomial. As a normalization check,
\[
\sum_r q^rk_r(q)=q^{16}(1+N_2(q)+N_4(q))+q^{26}(q^5-1)=q^{31}.
\]
The only central elements have odd component in \(\bigwedge^5V\), proving \(|Z(G_q)|=q^{16}\). Every group commutator lies in \(1+P\): factoring an arbitrary unit into its central even factor and a unit \(1+u\) with \(u\in O\), two such odd units satisfy \([1+u,1+w]=1+2u\wedge w\), which is central. Since generators \(1+e_i\) and \(1+e_j\) do not commute when \(i\ne j\), the nilpotency class is exactly two.

**5. Characteristic two and full units.** In characteristic two the exterior relations imply \(e_ie_j=e_je_i\) for every pair of generators, so \(E\) is commutative and every element of \(G_q\) forms its own conjugacy class. Finally, every unit of \(E\) has a unique factorization into a nonzero scalar and a principal unit, and scalars are central. This gives the full-unit-group statement.

## Verification
The accompanying standalone `verify.py` uses exact exterior multiplication in the squarefree basis. It exhaustively classifies all \(3^{10}=59049\) ternary degree-three forms by the rank of the associated alternating \(5\)-by-\(5\) matrix, obtaining \(1,2420,56628\) forms of ranks \(0,2,4\). It checks the odd-to-even multiplication ranks for deterministic samples over the prime fields of orders \(3,5,7\), and independently computes products, inverses and commutators of sampled principal units over orders \(2,3,5\). It checks mass conservation and the class-size formula for orders \(3,5,7,11\). Executing `python3 verify.py` yields `VERIFY_OK`.

These checks corroborate the proof. The infinite family of prime powers is covered by the algebraic and alternating-form arguments, not by extrapolation from finite samples.

## Relationship to prior work
Domokos and Zubor (2014 preprint, 2015 journal article) established the structure and maximal dimensions of commutative subalgebras of exterior algebras; their Proposition 7.5 already implies the uniform dimension of an element centralizer when its degree-one component is nonzero. This known ingredient is acknowledged. Their paper does not state the rank-two/rank-four degree-three distribution or the present complete conjugacy-class-size polynomial for principal units. Bovdi and Leung (2018 preprint, 2019 article) classify constructions of maximal commutative subalgebras, not individual finite-field conjugacy classes.

Rossmann (2021) obtains class-size polynomials for graphical groups built from independent graph-edge commutators. The present unit group's commutator map also has interactions between linear and cubic exterior degrees, and is not immediately determined by a graphical-group polynomial. Earlier finite-field work on the four-generator exterior algebra's associative commutator fibers concerns a smaller algebra and does not supply the new five-generator alternating-rank split.

## Limitations
The explicit spectrum is proved for the five-generator exterior algebra, not for arbitrary generator number. It does not count irreducible character degrees or conjugacy-class products. A complete literature-exhaustiveness certificate is not claimed: specialized work on finite Grassmann-algebra unit groups might contain equivalent formulas. The class-two assertion concerns the finite principal unit group, not the multiplication nilpotency index of the augmentation ideal.

## References
1. M. Domokos and M. Zubor, *Commutative subalgebras of the Grassmann algebra*, arXiv:1403.2916 (first public 12 March 2014); *Journal of Algebra and Its Applications* 14 (2015), 1550125. Full text: https://real.mtak.hu/33679/1/1403.2916v2.pdf.
2. V. A. Bovdi and H.-H. Leung, *Maximal commutative subalgebras of a Grassmann algebra*, arXiv:1803.03457 (9 March 2018); *Journal of Algebra and Its Applications* 18 (2019), 1950139.
3. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields* (2021), https://torossmann.github.io/files/csp.pdf.
