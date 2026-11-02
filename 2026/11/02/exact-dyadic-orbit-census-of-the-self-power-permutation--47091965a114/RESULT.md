# Exact dyadic orbit census of the self-power permutation

## Finding
For every integer \(k\ge1\), consider the map \(f_k(x)=x^x\pmod{2^k}\) on odd residue classes. It is well defined because an odd unit has multiplicative order dividing \(2^{\max(0,k-2)}\). The map is a permutation; in particular, **every state is periodic**, with no nonperiodic incoming trees.

For \(k=1\) there is one fixed state. For \(k\ge2\) the two classes \(x=1\) and \(x=-1\) are fixed. For all other odd classes the **exact least period** \(L_k(x)\) is as follows:

* If \(x\equiv1\pmod4\), set \(u=\nu_2(x-1)\), necessarily \(2\le u\le k-1\). Then
  \[L_k(x)=2^{\max(0,k-2u)}.\]
* If \(x\equiv3\pmod4\), set \(r=\nu_2(x+1)\), necessarily \(2\le r\le k-1\). Then
  \[L_k(x)=\begin{cases}1,&k\le r+1,\\2^{\max(1,k-3r+1)},&k>r+1.\end{cases}\]

These give the **complete cycle census** without orbit enumeration. Each fixed valuation layer \(u\) on the positive side has exactly \(2^{k-u-1}\) states, each of period \(L_+(k,u)\), and each layer \(r\) on the negative side has exactly \(2^{k-r-1}\) states, each of period \(L_-(k,r)\). Thus for every integer \(j\ge0\) and \(k\ge2\), writing \({\bf1}[Q]\) for the indicator of a proposition \(Q\), the exact number of cycles of length \(2^j\) is
\[
C_k(2^j)=2{\bf1}[j=0]
+\sum_{u=2}^{k-1}\frac{2^{k-u-1}}{L_+(k,u)}{\bf1}[L_+(k,u)=2^j]
+\sum_{r=2}^{k-1}\frac{2^{k-r-1}}{L_-(k,r)}{\bf1}[L_-(k,r)=2^j].
\]
All other cycle lengths have multiplicity zero. In particular, for every \(k\ge6\), the maximum period is \(2^{k-4}\) and **exactly two cycles** attain it. At \(k=8\), cycle counts for lengths \(1,2,4,8,16\) are respectively \(18,15,4,4,2\).

## Assumptions and scope
The input is an arbitrary odd residue modulo an exact power of two; a representative \(1\le x<2^k\) is used for integer exponentiation. The formulas do not depend on that representative. For nonendpoint layers the valuations refer to the chosen representative only when it is not the corresponding endpoint; equivalently they are the unique valuations in \([2,k-1]\) determined by the residue. Work in the 2-adic principal-unit group \(U=1+4\mathbb Z_2\), on which the 2-adic logarithm and exponential converge and satisfy \(\nu_2(\log z)=\nu_2(z-1)\). Throughout, \(\nu_2\) is the usual normalized 2-adic valuation. Statements are for every \(k\ge1\), with no unverified asymptotic assumptions.

## Proof
**1. Splitting the two sign components.** Every odd 2-adic integer is uniquely \(x=\varepsilon z\), where \(\varepsilon\in\{1,-1\}\) and \(z\in U\). Since the integer exponent \(x\) is odd, under this coordinate the self-power map preserves the sign and acts on \(z\) as
\[
F(z)=z^z=\exp(z\log z)\quad(\varepsilon=1),\qquad
G(z)=z^{-z}=\exp(-z\log z)\quad(\varepsilon=-1).
\]
These formulas agree with ordinary modular exponentiation and are 1-Lipschitz. Indeed for \(z,w\in U\), the difference between \(z\log z\) and \(w\log w\) is \((z-w)\log z+w(\log z-\log w)\). The first summand has valuation at least \(\nu_2(z-w)+2\), and the second exactly \(\nu_2(z-w)\); hence both \(F\) and \(G\) are 2-adic isometries. Consequently each induces a bijection of the corresponding finite residue classes, proving that the original map is a permutation.

**2. A displacement-lifting lemma.** Suppose \(T:U\to U\) is 1-Lipschitz and its displacement \(D(z)=T(z)-z\) obeys
\[\nu_2(D(z)-D(w))\ge\nu_2(z-w)+2\quad(z,w\in U).\]
If \(t=\nu_2(D(z))<\infty\), then
\[\nu_2(T^{2^a}(z)-z)=t+a\qquad(a=0,1,2,\ldots).\]
For the first doubling, \(T^2(z)-z=2D(z)+D(Tz)-D(z)\), where the two summands have valuations \(t+1\) and at least \(t+2\). Moreover the new displacement \(D_2=D+D\circ T\) is again 2-step Lipschitz, since \(T\) is 1-Lipschitz. Induction on repeated squaring gives the displayed equality. In particular the exact least period modulo \(2^k\), once some power-of-two iterate fixes the point, is \(2^{\max(0,k-t)}\).

**3. The positive-sign layers.** For \(z\in U\), write \(h(z)=(z-1)\log z\). Then
\[F(z)=z\exp(h(z)),\qquad D_F(z)=z(\exp(h(z))-1).\]
The product-difference identity and \(\nu_2(\log z)\ge2\) show \(\nu_2(h(z)-h(w))\ge\nu_2(z-w)+2\); the exponential is isometric on \(4\mathbb Z_2\). Therefore \(D_F\) satisfies the lemma's Lipschitz condition. For \(u=\nu_2(z-1)\ge2\), we have \(\nu_2(h(z))=2u\), hence \(\nu_2(D_F(z))=2u\). The lemma yields \(L_+(k,u)=2^{\max(0,k-2u)}\). The point \(z=1\) is fixed.

**4. The negative-sign layers.** For \(z\in U\),
\[G(z)=z^{-z},\qquad G(z)-z=z\bigl(\exp(-(z+1)\log z)-1\bigr).\]
Since \(\nu_2(z+1)=1\), if \(r=\nu_2(z-1)\), the first-step displacement is exactly \(r+1\). Thus \(G(z)\equiv z\pmod{2^k}\) exactly when \(k\le r+1\).

Otherwise examine the **exact second iterate**
\[H(z)=G^2(z)=z^{z^{1-z}}=z\exp\bigl(E(z)\log z\bigr),\quad E(z)=\exp((1-z)\log z)-1.\]
Here \(\nu_2(E(z))=2r\) and therefore \(\nu_2(H(z)-z)=3r\). More strongly, the map \(q(z)=(1-z)\log z\) is 2-step Lipschitz; consequently \(E(z)\) is 2-step Lipschitz and has valuation at least 4. Multiplication by \(\log z\), followed by exponential and multiplication by \(z\), shows that \(D_H=H-\mathrm{id}\) is at least 2-step Lipschitz. Apply the lemma to \(H=G^2\): the exact period of \(G\), known to be even when \(k>r+1\), is \(2^{\max(1,k-3r+1)}\). The point \(z=1\), corresponding to \(x=-1\), is fixed.

**5. Counting cycles.** For every valuation \(s\in\{2,\ldots,k-1\}\), the number of classes in a sign component with \(\nu_2(z-1)=s\) is exactly \(2^{k-s-1}\). By the established exact period law and bijectivity, partitioning each layer into orbits of that common length gives the two finite sums above. The endpoints are distinct fixed points for \(k\ge2\); for \(k=1\) there is only one residue. For \(k\ge6\), the largest positive-layer length occurs at \(u=2\) and equals \(2^{k-4}\); the remaining layers, including all negative layers, have smaller lengths. The \(2^{k-3}\) states at \(u=2\) form exactly two longest cycles. This proves the complete classification.

## Verification
A standalone standard-library verifier constructs the map independently with Python's modular exponentiation, traces every orbit, and checks bijectivity and the predicted period of **every** odd state for \(1\le k\le15\). It checks cycle-count formula, total state count, and the two-maximal-cycle consequence when \(k\ge6\). Execute `python3 verify_self_power.py`. This finite check corroborates but does not replace the uniform 2-adic proof above.

## Relationship to prior work
Holden, Richardson and Robinson (arXiv:1609.06696, publicly posted 21 September 2016, revised 2020) analyze the same self-power map at prime powers. Their Sections 3 and 5 count fixed points and two-cycles, respectively; their Section 6 explicitly addresses longer rooted closed walks as future work. They develop general interpolation techniques, which are background here, but their checked 2020 text does not give the exact least periods or complete dyadic cycle census. Min Sha (arXiv:1101.3482) examines iteration of maps with **fixed** exponent; the exponent in the present map varies with the current state. Friedrichsen and Holden (arXiv:1403.5548) study fixed-point statistics modulo primes. The period-law and full-cycle-count statement are the contribution assessed here; the classical 2-adic logarithm and elementary lifting methods are not claimed as new.

## Limitations
The classification covers odd units modulo powers of two and no other prime powers or even inputs. Originality is not guaranteed against all historical literature: in particular, early work on residues of \(n^n\) by Crocker has not been fully inspected, and an equivalent theorem might appear in another specialized source. Finite code cannot certify the infinite proof. No independent audit has been performed.

## References
1. J. Holden, P. A. Richardson, M. M. Robinson, *Counting fixed points and rooted closed walks of the singular map modulo powers of a prime*, arXiv:1609.06696, first submitted 2016-09-21, version 3 (2020), Sections 1, 3, 5 and 6. https://arxiv.org/pdf/1609.06696
2. M. Sha, *On the dynamics of power maps*, arXiv:1101.3482 (2011). https://arxiv.org/abs/1101.3482
3. M. Friedrichsen and J. Holden, *Statistics for fixed points of the self-power map*, arXiv:1403.5548 (2014). https://arxiv.org/abs/1403.5548
4. R. Crocker, work on residues of \(n^n\) (1960s), cited as early background in reference 1; complete full text not inspected.
