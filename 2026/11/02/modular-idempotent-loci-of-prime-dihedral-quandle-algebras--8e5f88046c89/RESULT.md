# Modular idempotent loci of prime dihedral quandle algebras

## Finding

For every odd prime \(p\) and every field \(k\) of characteristic \(p\), let \(R_p=\mathbb Z/p\mathbb Z\) carry the dihedral quandle operation \(i\triangleleft j=2j-i\), and let \(k[R_p]\) denote its (generally nonassociative) quandle algebra. Write \(\mathcal E_p\) for the affine scheme of solutions \(u\star u=u\). Define \(o_p=\operatorname{ord}_p(2)\), \(\ell_p=\operatorname{lcm}(2,o_p)\), and \(d_p=(p-1)/\ell_p\). Then there is a \(k\)-scheme isomorphism

\[
\mathcal E_p\cong \operatorname{Spec}k\ \sqcup\ \mathbb A_k^{d_p}.
\]

The singleton consists of zero; the affine component consists exactly of augmentation-one idempotents. In particular, for every prime power \(q=p^e\),

\[
\#\{u\in\mathbb F_q[R_p]:u\star u=u\}=1+q^{d_p}.
\]

For \(p=17\), the affine component has dimension two, so the count over \(\mathbb F_{17}\) is \(290\); for \(p=31\) it has dimension three and the count over \(\mathbb F_{31}\) is \(29792\). The basis idempotents are only \(p\) points of the affine component; hence non-basis idempotents occur in both examples. The previously known three-element case \(p=3\) is recovered but is not claimed as new.

## Assumptions and scope

The prime \(p\) is odd; the coefficient field has characteristic exactly \(p\), but need not be finite or algebraically closed. The algebra \(k[R_p]\) has basis \(e_i\), with \(e_i\star e_j=e_{2j-i}\). In this work “idempotent” means a solution to the single equation \(u\star u=u\); associativity is *not* assumed. The scheme claim concerns the full affine functor of solutions over commutative \(k\)-algebras, not merely the reduced set of points. The *auxiliary* group ring used below is associative and is distinct from the quandle algebra.

## Proof

**Step 1: Convert quandle multiplication to a polynomial identity.** Identify the underlying vector space with the associative group ring \(B=k[X]/(X^p-1)\) by \(e_i\leftrightarrow X^i\). Define \(\sigma_aF(X)=F(X^a)\) for \(a\in\mathbb F_p^\times\). A basis computation gives

\[
F\star G=(\sigma_{-1}F)(\sigma_2G)
\]

with the multiplication on the right taken in \(B\). Thus \(F\) is idempotent precisely when

\[
F=(\sigma_{-1}F)(\sigma_2F).
\]

**Step 2: Separate augmentations, including scheme-theoretically.** Let \(\varepsilon(F)=F(1)\). Applying augmentation yields \(c=c^2\). Since \(c(c-1)=0\), the affine solution scheme decomposes into the open-and-closed loci \(c=0\) and \(c=1\); this remains true after arbitrary commutative base change. Put \(T=X-1\). In characteristic \(p\), \(B\cong k[T]/(T^p)\), with augmentation ideal \(\mathfrak m=(T)\). Every \(\sigma_a\) preserves \(\mathfrak m\). If \(c=0\), the idempotence equation implies successively \(F\in\mathfrak m^{2^h}\) for every \(h\ge0\). Since \(\mathfrak m^p=0\), this forces \(F=0\) over every base ring; the zero component is exactly \(\operatorname{Spec}k\), not a thickened point.

**Step 3: Polynomial logarithm linearizes the augmentation-one locus.** For \(c=1\), write \(F=1+v\), \(v\in\mathfrak m\). The truncated series

\[
\log(1+v)=\sum_{j=1}^{p-1}\frac{(-1)^{j-1}v^j}{j},\qquad
\exp(H)=\sum_{j=0}^{p-1}\frac{H^j}{j!}
\]

are inverse polynomial isomorphisms between \(1+\mathfrak m\) under multiplication and \(\mathfrak m\) under addition; the denominators used are units in characteristic \(p\). They commute with the substitutions \(\sigma_a\). Consequently, writing \(F=\exp(H)\), the idempotence equation is equivalent to

\[
(\sigma_{-1}+\sigma_2-\mathrm{id})H=0.
\]

The augmentation-one locus is therefore a linear kernel transported by a polynomial automorphism, so it is already an affine space as a scheme.

**Step 4: Determine the kernel dimension without passing to a field extension.** The multiplicative group \(\mathbb F_p^\times\) acts on \(\mathfrak m\) through the \(\sigma_a\); its order \(p-1\) is invertible in \(k\). Hence the representation is semisimple by averaging. Its stable filtration

\[
\mathfrak m\supset\mathfrak m^2\supset\cdots\supset\mathfrak m^{p-1}\supset0
\]

has one-dimensional quotients \(\mathfrak m^j/\mathfrak m^{j+1}\), for \(1\le j\le p-1\), on which \(\sigma_a\) acts as multiplication by \(a^j\), because \((1+T)^a-1\equiv aT\pmod{T^2}\). Thus \(\mathfrak m\) is the direct sum of precisely these \(p-1\) characters (each appears once). On character \(j\), the displayed linear operator has eigenvalue \((-1)^j+2^j-1\). For even \(j\) it is \(2^j\ne0\); for odd \(j\) it vanishes exactly when \(2^{j-1}=1\pmod p\). This is equivalent to \(j\equiv1\pmod{\operatorname{lcm}(2,o_p)}\). Exactly \((p-1)/\ell_p\) integers in \(1\le j\le p-1\) satisfy this congruence. The kernel has dimension \(d_p\), proving both the scheme decomposition and the finite-field count. \(\square\)

## Verification

The bundled `verify.py` uses finite-field row reduction to reconstruct the kernel of \(\sigma_{-1}+\sigma_2-I\) independently of the character argument, for \(p=3,5,7,11,13,17,19,23,31\). It also constructs nonlinear idempotents by truncated exponentials and checks the original bilinear quandle multiplication for the two dimension-jump primes. An exhaustive coefficient enumeration checks \(p=3\) and \(p=5\) directly (all \(p^p\) elements), checking predicted counts and augmentations without invoking logarithms. These finite tests are not a proof for arbitrary primes or fields; the proof above is uniform.

## Relationship to prior work

Carter, Crans, Elhamdadi and Saito (2006) explicitly use dihedral quandles and linearized quandle operations, establishing an archive-era algebraic starting point. Bardakov, Passi and Singh (2017) develop the theory of quandle rings and augmentation ideals; their 2010 MSC list includes \(17D99\) as a relevant classification. Elhamdadi et al. (2020) investigate integral quandle-ring idempotents, particularly the three-element dihedral case. Bardakov and Elhamdadi (2026) analyze integral augmentation-ideal powers for dihedral quandles and selected idempotents. Elhamdadi, Ta and Virgin (2026) use Fourier methods to prove integral rigidity for odd dihedral quandles. Integral coefficient restrictions do not imply the characteristic-\(p\) statement here, which has positive-dimensional families and new dimension jumps. A published mathematical-record result already identifies the \(p=3\), characteristic-three affine line; its claim is explicitly subsumed, not claimed as original. The asserted contribution is the uniform all-odd-prime modular affine-scheme classification and arithmetic order-of-two dimension formula.

## Limitations

The theorem treats characteristic equal to an odd prime quandle size; it does not classify prime-power or composite quandle orders, mismatched characteristics, quandle-algebra automorphism orbits, or idempotents of more general Alexander quandles. Implicit appearance of a similar general theorem in uninspected literature remains a publication-priority risk. The full scheme statement refers to the affine equation \(u\star u=u\), not an associative algebra idempotent scheme.

## References

1. Carter, Crans, Elhamdadi and Saito, *Cohomology of Categorical Self-Distributivity*, arXiv:math/0607417 (first public 2006-07-18), https://arxiv.org/abs/math/0607417.
2. Bardakov, Passi and Singh, *Quandle rings*, arXiv:1709.03069 (2017), https://arxiv.org/abs/1709.03069.
3. Elhamdadi et al., *Zero-divisors and idempotents in quandle rings*, arXiv:2001.06843 (2020), https://arxiv.org/abs/2001.06843.
4. Bardakov and Elhamdadi, *Idempotents and Powers of Ideals in Quandle Rings*, arXiv:2601.07057 (2026), https://arxiv.org/abs/2601.07057.
5. Elhamdadi, Ta and Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799 (2026), https://arxiv.org/abs/2609.03799.
6. Published published-finding corpus finding `2026/10/4/SCOPE-a-characteristic-three-idempotent-line-in-the-quandle-algebra-of--06aa9c19e539` (special \(p=3\) case), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-a-characteristic-three-idempotent-line-in-the-quandle-algebra-of--06aa9c19e539.
