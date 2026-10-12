# Prime-by-prime rationality spectrum of the 72 type-nine points on the Fermat cubic

## Finding

Let \(F\subset\mathbb P^2_{\mathbb Q}\) be \(X^3+Y^3+Z^3=0\), equipped with elliptic origin \(O=[1:-1:0]\). The 72 geometric type-nine points are the exact-order-nine points \(T=F[9]\setminus F[3]\). For **every prime** \(p\ge5\), put \(N_p=|T(\mathbb F_p)|\). Then

\[
N_p=\begin{cases}
72,&p\equiv1\pmod9\text{ and }3^{(p-1)/3}\equiv1\pmod p,\\
18,&p\equiv1\pmod9\text{ and }3^{(p-1)/3}\not\equiv1\pmod p,\\
6,&p\equiv8\pmod9,\\
0,&p\equiv2,4,5,7\pmod9.
\end{cases}
\]

The natural densities of prime sets with \(N_p=0,6,18,72\) are respectively \(2/3,1/6,1/9,1/18\). Furthermore, the field defining all 72 individual points is exactly
\[K=\mathbb Q(F[9])=\mathbb Q(\sqrt[3]{3},\zeta_9),\qquad[K:\mathbb Q]=18.\]
The rationality count refers to geometric type-nine points fixed by Frobenius; no assertion is made about the number of all rational points on \(F\).

## Assumptions and scope

The coefficient field is \(\mathbb Q\); every reduction is at a prime \(p\ge5\), so the cubic is smooth and multiplication by 9 is separable. The origin is the rational flex \(O\). A type-nine point means a point admitting irreducible order-nine contact by a plane cubic, as in the cited geometric literature, and not a flex; on a smooth elliptic plane cubic these are precisely the non-three-torsion points killed by 9. Rationality of such a point means its coordinates lie in \(\mathbb F_p\), not that a chosen equation for an osculating cubic is rational.

## Proof

**1. Elliptic and torsion models.** Set \(E:v^2=u^3-432\). Off \(O\), the rational transformation
\[u=-12Z/(X+Y),\qquad v=36(X-Y)/(X+Y)\]
is an isomorphism \(F\to E\), sending \(O\) to infinity. Abel's theorem identifies the plane type-nine points with \(E[9]\setminus E[3]\), of cardinality \(81-9=72\) over an algebraic closure. The 3-division polynomial is \(3u(u^3-1728)\). Its nonzero torsion points have \(u=0,v=\pm12\sqrt{-3}\), or \(u=12\omega^j,v=\pm36\) for \(j=0,1,2\), where \(\omega^2+\omega+1=0\). All of \(E[3]\) is consequently defined over \(L=\mathbb Q(\omega)\).

**2. The exact nine-division field.** Put \(\alpha=\sqrt[3]{3}\) and let \(\beta=\zeta_9\). Merta--Zięba's explicit enumeration proves \(E[9]\subset E(\mathbb Q(\alpha,\beta))\). Conversely, the Weil pairing on \(E[9]\) puts \(\beta\) in \(\mathbb Q(E[9])\). One of their exact-order-nine points on \(F\) is
\[
[3:\alpha\beta(\beta^4+2\beta^3-\beta+1):
-\alpha^2(\beta^2+\beta+1)(\beta^3-\beta+1)].
\]
The factor \(\beta^4+2\beta^3-\beta+1\) is nonzero, since its degree is less than the minimal polynomial \(\Phi_9(T)=T^6+T^3+1\). The ratio of the first two coordinates therefore recovers \(\alpha\) once \(\beta\) is known. Thus \(\mathbb Q(E[9])=K=\mathbb Q(\alpha,\beta)\). Because \(\mathbb Q(\beta)/\mathbb Q\) is abelian Galois whereas \(\mathbb Q(\alpha)/\mathbb Q\) is nonnormal cubic, \(\alpha\notin\mathbb Q(\beta)\). Hence \([K:\mathbb Q]=3\varphi(9)=18\) and \([K:L]=9\).

**3. Complex multiplication and split Frobenius.** The automorphism \((u,v)\mapsto(\omega u,v)\) endows the torsion with an action of \(R=\mathbb Z[\omega]\) over \(L\). With \(\pi=1-\omega\), one has \(\pi^2=-3\omega\); hence \(E[9]=E[\pi^4]\). Since the kernel of \([\pi^j]\) has size \(3^j\) for \(j=1,\ldots,4\), the module \(E[9]\) is free of rank one over \(R/9R\). The full 3-torsion is \(L\)-rational, so \(\operatorname{Gal}(K/L)\) acts via units congruent to 1 modulo 3. Both this group and \(\operatorname{Gal}(K/L)\) have order 9, giving an isomorphism
\[
\operatorname{Gal}(K/L)\simeq1+3R/9R\simeq(R/3R,+).
\]
The ring \(R/3R\simeq\mathbb F_3[\epsilon]/(\epsilon^2)\), with \(\epsilon=1-\omega\). For any prime \(p\equiv1\pmod3\), arithmetic Frobenius acts on \(E[9]\) as multiplication by \(1+3a\), where \(a\in R/3R\). The kernel of multiplication by \(3a\) on \(R/9R\) has size 81 if \(a=0\), 27 if \(a\) is either of the two nonzero nilpotents \(\epsilon,2\epsilon\), and 9 for the other six (unit) values of \(a\). Subtracting the 9 rational three-torsion points gives \(N_p=72,18,0\), respectively.

The Weil pairing gives \(p\equiv\det(\operatorname{Frob}_p|E[9])\equiv\operatorname{Norm}_{R/\mathbb Z}(1+3a)\equiv1+3\operatorname{Tr}_{R/\mathbb Z}(a)\pmod9\). Modulo 3, the trace has kernel precisely \(\{0,\epsilon,2\epsilon\}\). Thus \(p\equiv1\pmod9\) gives \(a=0\) or a nonzero nilpotent, while \(p\equiv4,7\pmod9\) forces a unit and \(N_p=0\). In the \(p\equiv1\pmod9\) case, \(a=0\) exactly when \(p\) splits completely in \(K\). Since \(\beta\) already belongs to \(\mathbb F_p\), this is equivalent to \(\alpha\in\mathbb F_p\), equivalently \(3^{(p-1)/3}\equiv1\pmod p\). This establishes both cases with \(p\equiv1\pmod9\).

**4. Inert Frobenius.** For \(p\equiv2\pmod3\), cubing permutes \(\mathbb F_p\). Consequently \(\#E(\mathbb F_p)=p+1\), since \(\sum_{u\in\mathbb F_p}\chi(u^3-432)=\sum_{t\in\mathbb F_p}\chi(t-432)=0\). The division polynomial above shows exactly three elements of \(E[3](\mathbb F_p)\): infinity and \((12,\pm36)\). Thus the 3-primary subgroup is cyclic and \(|E[9](\mathbb F_p)|=\gcd(9,p+1)\). When \(p\equiv8\pmod9\) this is 9, hence \(N_p=6\); when \(p\equiv2,5\pmod9\) it is 3, hence \(N_p=0\).

**5. Densities.** The 18-element Galois group \(\operatorname{Gal}(K/\mathbb Q)\) has an index-two subgroup of nine elements \(\operatorname{Gal}(K/L)\). In the latter, the three cases above have respectively 1, 2 and 6 elements; they are invariant under conjugation. Chebotarev therefore yields density \(1/18\) for 72, density \(2/18=1/9\) for 18, and density \(6/18=1/3\) for 0 among split primes. Dirichlet's theorem gives density \(1/6\) for \(p\equiv8\pmod9\), producing 6; the remaining two inert residue classes contribute another \(1/3\) to 0. The total density for zero is \(2/3\).

## Verification

The accompanying standalone \(\texttt{verify.py}\) checks the displayed algebraic type-nine representative exactly in the quotient with \(\alpha^3=3\) and \(\Phi_9(\beta)=0\). It independently enumerates the finite-field group \(E(\mathbb F_p)\) for primes \(5\le p<1100\), computes the kernels of multiplication by 3 and by 9 using rational elliptic-curve formulas modulo \(p\), and compares their difference to the four-case prediction. These finite tests support, but do not replace, the CM/Frobenius argument and Chebotarev proof, which establish the infinite claim.

## Relationship to prior work

Gattazzo (1979) proved the general geometric type-nine count of 72 and gave an algebraic construction. Szemberg--Szpond (2022) posed coordinate questions for the Fermat cubic. Merta--Zięba (2024) supplied all 72 coordinates over \(K\), but not the exact minimal nine-division field, finite-field rationality cases or their natural prime densities. The geometric projective automorphism orbit decomposition of these same 72 points into orbits of sizes 18 and 54 addresses a different group action and does not imply the Frobenius-count classification. Classical complex multiplication, Weil pairing and Chebotarev are ingredients, not claimed as new theorems.

## Limitations

The result applies to the fixed Fermat cubic and prime fields in characteristic at least five, not arbitrary plane cubics or all finite extensions. All statements about prime densities are natural densities of rational primes, not finite-sample frequencies. The script's finite calculations do not independently certify Chebotarev or an infinite classification. The possibility of an unindexed earlier arithmetic computation remains a bibliographic risk.

## References

1. Ł. Merta and M. Zięba, *Sextactic and type-9 points on the Fermat cubic and associated objects*, arXiv:2406.13802v1 (first public 2024-06-19), Sections 1--2, Theorem A, explicit type-nine coordinates. https://arxiv.org/pdf/2406.13802
2. T. Szemberg and J. Szpond, *Sextactic points on the Fermat cubic curve and arrangements of conics*, arXiv:2211.00494v1 (2022), geometric precursor and coordinate problems. https://arxiv.org/pdf/2211.00494
3. R. Gattazzo, *Punti di tipo 9 di una cubica ellittica*, Rendiconti del Seminario Matematico della Università di Padova 61 (1979), 285--301, especially Proposition 3.3. https://www.numdam.org/item/RSMUP_1979__61__285_0.pdf
