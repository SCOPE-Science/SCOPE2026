# A complete modular idempotent-quandle classification for prime-order affine quandles

## Finding
Let \(p\) be an odd prime, \(k\) a field of characteristic \(p\), and \(\lambda\in\mathbb F_p\setminus\{0,1\}\). Define an affine quandle \(Q_{p,\lambda}=\mathbb F_p\) by \(i\triangleright j=(1-\lambda)i+\lambda j\), and its nonassociative \(k\)-algebra \(A=k[Q_{p,\lambda}]\) by bilinear extension of the quandle product. Write \(a=1-\lambda\), \(b=\lambda\), and define the resonance set
\[
J_{p,\lambda}=\{j\in\{1,\ldots,p-1\}:a^j+b^j=1\text{ in }\mathbb F_p\}.
\]
Every nonzero idempotent belongs to a subquandle of \(A\), and there is an explicit quandle isomorphism from it onto the additive-vector-space Alexander quandle on \(k^{J_{p,\lambda}}\):
\[
(x_j)\triangleright(y_j)=(a^jx_j+b^jy_j)_{j\in J_{p,\lambda}}.
\]
Zero is the only other idempotent. In particular, when \(k=\mathbb F_q\), \(q=p^f\), their number is exactly \(1+q^{d_{p,\lambda}}\), with \(d_{p,\lambda}=|J_{p,\lambda}|\). These are actual elements of the bilinear quandle algebra; the zero element is not included in the idempotent subquandle.

## Assumptions and scope
The quandle is cyclic of prime order and connected/Latin: both \(a\) and \(b\) are nonzero, and \(a+b=1\). The coefficient field has characteristic equal to the underlying prime order. The result holds over arbitrary fields \(k\) of this characteristic; only the cardinality statement assumes \(k\) finite. All powers, exponential, and logarithmic operations below are computed in a *separate associative* cyclic group algebra, never using associative identities for the original quandle multiplication.

## Proof
Identify the underlying vector space of \(A\) with the associative algebra \(B=k[t]/(t^p-1)=k[u]/(u^p)\), where \(u=t-1\), by sending the basis vector indexed by \(i\) to \(t^i\). Denote the multiplication in \(B\) by juxtaposition, and the nonassociative multiplication in \(A\) by \(\star\). For \(c\in\mathbb F_p^\times\), the algebra automorphism \(\sigma_c\) of \(B\) is defined by \(\sigma_c(t)=t^c\). Expanding two vectors in the basis shows directly that
\[
F\star G=\sigma_a(F)\sigma_b(G).
\]
Let \(\epsilon:B\to k\) be the augmentation, \(\epsilon(t)=1\), and let \(I=(u)\). Since \(\epsilon(F\star F)=\epsilon(F)^2\), every idempotent has augmentation zero or one. If it is zero, then \(F\in I\) and \(F=\sigma_a(F)\sigma_b(F)\in I^2\). Repeating this identity puts \(F\) in \(I^{2^r}\) for all \(r\), and \(I^p=0\), forcing \(F=0\).

For a nonzero idempotent, \(\epsilon(F)=1\); thus \(F\in1+I\). The truncated polynomial maps
\[
\log(1+z)=\sum_{h=1}^{p-1}(-1)^{h+1}z^h/h,
\quad
\exp(z)=\sum_{h=0}^{p-1}z^h/h!
\]
are mutually inverse between the multiplicative abelian group \(1+I\) and the additive group \(I\). This follows from the ordinary formal identities modulo total degree \(p\), whose denominators in degrees below \(p\) are units in \(k\). In particular, \(\log(XY)=\log X+\log Y\) for \(X,Y\in1+I\), and both maps commute with each \(\sigma_c\).

Put \(v=\log(t)=\log(1+u)\). Its linear term in \(u\) is \(u\), hence \(v,v^2,\ldots,v^{p-1}\) form a basis of \(I\). The identity \(\sigma_c(v)=\log(t^c)=c v\) gives \(\sigma_c(v^j)=c^jv^j\). Therefore, writing \(F=\exp(H)\) with \(H=\sum_{j=1}^{p-1}z_jv^j\), the idempotency equation is exactly
\[
F\star F=F\quad\Longleftrightarrow\quad
\sigma_a(H)+\sigma_b(H)=H\quad\Longleftrightarrow\quad
(a^j+b^j-1)z_j=0\text{ for each }j.
\]
The free coordinates are precisely those indexed by \(J_{p,\lambda}\); the parametrization is bijective. For two such elements \(F=\exp(H)\), \(G=\exp(K)\), the defining identity yields
\[
\log(F\star G)=\sigma_a(H)+\sigma_b(K)
 =\sum_{j\in J_{p,\lambda}}(a^jx_j+b^jy_j)v^j.
\]
Thus the nonzero idempotents are closed under \(\star\), and the coordinate law is the stated affine quandle law. On every coordinate both scalars are nonzero and sum to one; consequently every right translation and every left translation is bijective. The finite-field count follows because each of the \(d_{p,\lambda}\) coordinates takes \(q\) values, plus zero.

The index \(1\) always belongs to \(J_{p,\lambda}\); it accounts for the original \(p\) basis idempotents. Other indices give new idempotents. For example, at \((p,\lambda)=(7,3)\), \(J=\{1,5\}\) and the count over \(\mathbb F_7\) is \(50\); at \((13,4)\), \(J=\{1,5,7,11\}\) and the count is \(28{,}562\). At the midpoint parameter \(a=b=1/2\), the resonances are exactly \(j\equiv1\pmod{\operatorname{ord}_p(2)}\), so the nonzero-idempotent quandle is a midpoint quandle on \(k^d\). For \(p=31\), \(d=6\) and the count over \(\mathbb F_{31}\) is \(887{,}503{,}682\).

## Verification
The standalone standard-library Python file `verify_affine_quandle.py` independently computes the bilinear quandle product, cyclic-algebra truncated logarithms/exponentials, and resonance sets. It exhaustively enumerates all coefficient vectors in six configurations over \(\mathbb F_3,\mathbb F_5,\mathbb F_7\), compares them with the formula, and checks each explicitly parametrized element. It also checks degree-generator identities at five larger primes. A separate direct pairwise-product check verified all \(2{,}401\) products in each of the \((7,3)\) and \((7,4)\) 49-element nonzero-idempotent quandles. These tests are finite corroboration rather than an infinite proof. Reproduce the main tests with `python3 verify_affine_quandle.py`.

## Relationship to prior work
Carter, Crans, Elhamdadi, and Saito (2006) constructed self-distributive operations on vector spaces spanned by quandles, providing an archival algebraic starting point. Hulpke, Stanovský, and Vojtěchovský (2014) studied connected and affine quandles. Bardakov, Passi, and Singh (2017) formalized and studied quandle rings and their augmentation; the present calculation isolates the modular prime-order affine situation. A previous dihedral-specific modular result already covers the case \(\lambda=2\), including its exact affine dimension; that special case is explicitly *not* claimed as a new contribution. Elhamdadi, Ta, and Virgin (2026) studied integral and complex quandle-algebra idempotents using Fourier methods, including a character-eigenvalue condition; that is a different coefficient-characteristic regime, and their arguments do not directly determine modular idempotent counts or the induced quandle for all \(\lambda\). The present contribution is a uniform classification for every connected prime-order affine parameter with its internal quandle structure.

## Limitations
The theorem assumes the base quandle has prime order and the coefficient field has the same characteristic. It does not address composite cyclic orders, coefficients of other characteristics, or general finite connected quandles. A close methodological relationship to the earlier dihedral result remains; publication-priority and broader literature coverage require independent checking. The resulting quandle isomorphism and exact finite-field formula are mathematical statements; they are not claims of independent certification.

## References
- J. S. Carter, A. Crans, M. Elhamdadi, M. Saito, *Cohomology of Categorical Self-Distributivity*, arXiv:math/0607417, first public July 18, 2006, especially the vector-space quandle construction and Alexander-quandle background.
- A. Hulpke, D. Stanovský, P. Vojtěchovský, *Connected quandles and transitive groups*, arXiv:1409.2249, first public September 8, 2014.
- V. Bardakov, I. B. S. Passi, M. Singh, *Quandle Rings*, arXiv:1709.03069, first public September 2017.
- M. Elhamdadi, H. Ta, C. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799, 2026, particularly sections 4–6.
