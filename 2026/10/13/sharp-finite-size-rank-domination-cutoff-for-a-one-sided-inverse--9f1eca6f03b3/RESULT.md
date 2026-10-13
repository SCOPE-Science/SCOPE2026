# Sharp finite-size rank-domination cutoff for a one-sided inverse relation over finite fields

## Finding

Let \(q\) be a prime power and \(N\ge1\). Put \(k=\mathbb F_q\), let \(F=k\langle x,y\rangle\) be the unital free associative algebra, and set \(f=xy-1\). For \(g\in F\), write \(g\in\mathcal R_{q,N}\) if there is a constant \(C\ge0\), allowed to depend on \(g,q,N\), such that
\[
\operatorname{rank}g(X,Y)\le C\operatorname{rank}(XY-I_m)
\]
for every integer \(1\le m\le N\) and every \(X,Y\in M_m(k)\). The matrix identity has the usual unital evaluation convention. Let \(\pi:F\to k[t,t^{-1}]\) be the map \(\pi(x)=t\), \(\pi(y)=t^{-1}\).

Write \(\mathcal I_q\) for the collection of all monic irreducibles in \(k[t]\), excluding the polynomial \(t\), and define
\[
P_{q,N}(t)=\prod_{\substack{\varphi\in\mathcal I_q\\\deg\varphi\le N}}\varphi(t)^{\lfloor N/\deg\varphi\rfloor},\qquad D_{q,N}=\deg P_{q,N}.
\]
Products are finite, and \(P_{q,N}(0)\ne0\). All ideals denoted by parentheses below are two-sided in \(F\), or ordinary principal ideals when written inside the commutative Laurent ring.

**Theorem (bounded-size rank-domination ideal and sharp degree threshold).** For every \(q,N\) as above:

1. \(\mathcal R_{q,N}=\pi^{-1}((P_{q,N}))\). It suffices to test the rank inequality only at the single size \(m=N\), with a constant chosen independently of the matrices.
2. The unbounded class satisfies \(\bigcap_{N\ge1}\mathcal R_{q,N}=\ker\pi=(xy-1,yx-1)\). Thus global rank domination by \(xy-1\) is precisely membership in the indicated two-generator ideal, not necessarily in \((xy-1)\).
3. Among \(g\in\mathcal R_{q,N}\setminus\ker\pi\), the **minimum free-word degree** is exactly \(\lceil D_{q,N}/2\rceil\). For any nonnegative integer \(L\), a rank-domination test on all \(N\)-dimensional matrix pairs suffices to certify global rank domination for **every** candidate \(g\) of degree at most \(L\) if and only if \(2L<D_{q,N}\). At and above the threshold explicit counterexamples exist.

One may compute the threshold directly from the irreducible counts:
\[
D_{q,N}=\sum_{d=1}^{N}d\,I_q^{\times}(d)\left\lfloor\frac Nd\right\rfloor,
\]
where \(I_q^{\times}(1)=q-1\) and, for \(d\ge2\),
\[
I_q^{\times}(d)=\frac1d\sum_{e\mid d}\mu(e)q^{d/e}.
\]
In particular, \(D_{2,1}=1\), \(D_{2,2}=4\), \(D_{2,3}=11\), \(D_{3,1}=2\), and \(D_{3,2}=10\).

## Assumptions and scope

The coefficient field is **finite**; the prime-power condition includes nonprime fields. Every matrix is square and both free variables are evaluated at matrices of the **same** size. No invertibility hypothesis is imposed in the rank inequality, although its zero-denominator tests force invertibility. The word degree of a nonzero free polynomial is the largest length of a monomial with nonzero coefficient; constants have degree zero.

The assertion about a finite-size test concerns a fixed \(q\) and \(N\), and a uniform certification claim over the **entire degree-bounded class**, not that each particular low-degree polynomial is or is not dominated. The constant in the unbounded rank inequality may depend on the particular polynomial \(g\), but not on matrix size.

## Proof

**Step 1: Reduce bounded domination to zero tests.** If \(XY=I_m\) for square matrices, then \(X\) is invertible and \(Y=X^{-1}\). Hence the rank inequality forces \(g(X,X^{-1})=0\) on every invertible \(X\in\mathrm{GL}_m(k)\). Conversely, suppose those evaluations vanish for all \(m\le N\). If \(XY-I_m\ne0\), its rank is at least one, whereas \(\operatorname{rank}g(X,Y)\le m\le N\). Thus \(C=N\) suffices for every such pair. Vanishing on all invertible sizes \(m\le N\) is equivalent to vanishing at size \(N\) alone: replace \(X\) by \(X\oplus I_{N-m}\) and apply direct-sum compatibility of polynomial evaluation.

**Step 2: Determine the exact universal annihilator.** On inverse pairs, \(g(X,X^{-1})=\pi(g)(X)\); negative Laurent powers are legitimate because \(X\) is invertible. Write \(\pi(g)=t^{-a}h(t)\) with \(a\ge0\) and \(h\in k[t]\). The Laurent evaluation vanishes exactly when \(h(X)=0\). We prove that the polynomials vanishing on every invertible matrix of dimension at most \(N\) form \((P_{q,N})\) in \(k[t]\).

For any invertible matrix \(X\) of size \(m\le N\), the rational canonical form decomposes its underlying \(k[t]\)-module into elementary primary summands \(k[t]/(\varphi^{e})\), where \(\varphi\) is monic irreducible other than \(t\), and \(e\deg\varphi\le m\le N\). Thus the minimal polynomial of \(X\) divides \(P_{q,N}\), so \(P_{q,N}(X)=0\). Conversely, for each such \(\varphi\) of degree \(d\le N\), the companion matrix of \(\varphi^{\lfloor N/d\rfloor}\) is invertible, has size \(d\lfloor N/d\rfloor\le N\), and has that exact minimal polynomial. Any polynomial annihilating all tested matrices must be divisible by each indicated power, hence by their product. This proves part 1, including the Laurent-ideal formulation, because \(t\) is a unit in \(k[t,t^{-1}]\).

**Step 3: Pass from bounded to unbounded sizes.** The degrees \(D_{q,N}\) tend to infinity, since at least the factor \((t-1)^N\) divides \(P_{q,N}\). Hence a nonzero Laurent polynomial cannot belong to \((P_{q,N})\) for every \(N\): after multiplication by one power of \(t\), this would give nonzero ordinary polynomial multiples of arbitrarily high-degree \(P_{q,N}\). Therefore \(\bigcap_N\mathcal R_{q,N}=\ker\pi\). The kernel is \((xy-1,yx-1)\), since imposing these two relations makes \(x\) invertible with two-sided inverse \(y\), giving the universal Laurent polynomial algebra.

It remains to verify that this kernel is indeed the set of **globally** rank-dominated polynomials rather than only those vanishing on all inverse pairs. The elementary equal-rank identity
\[
\operatorname{rank}(XY-I_m)=\operatorname{rank}(YX-I_m)
\]
holds over any field, for all square \(X,Y\) (the maps \(Y\) and \(X\) give mutually inverse isomorphisms of the respective kernels). Every element of \((xy-1,yx-1)\) is a finite sum of left and right polynomial multiples of these two generators. Subadditivity of rank and \(\operatorname{rank}(ABC)\le\operatorname{rank}(B)\) provide a global constant equal to the number of summands. Conversely, any globally dominated polynomial belongs to every \(\mathcal R_{q,N}\), so belongs to their intersection.

**Step 4: The lower degree bound and equality construction.** Suppose \(g\in\mathcal R_{q,N}\setminus\ker\pi\) has word degree \(L\). Each monomial of length at most \(L\) maps to one Laurent monomial \(t^j\) with \(-L\le j\le L\). Thus \(t^L\pi(g)\) is a nonzero ordinary polynomial of degree at most \(2L\), divisible by \(P_{q,N}\). Consequently \(2L\ge D_{q,N}\), giving \(L\ge\lceil D_{q,N}/2\rceil\).

For equality, set \(L=\lceil D_{q,N}/2\rceil\) and expand \(t^{-L}P_{q,N}(t)\). Its exponents lie between \(-L\) and \(D_{q,N}-L\le L\). Define \(g_{q,N}\in F\) by replacing each term \(c_jt^j\) with \(c_jx^j\) when \(j\ge0\), and \(c_jy^{-j}\) when \(j<0\). Then \(\pi(g_{q,N})=t^{-L}P_{q,N}\ne0\), and \(g_{q,N}\in\mathcal R_{q,N}\). Since \(P_{q,N}(0)\ne0\), the term of exponent \(-L\) is present, so \(\deg g_{q,N}=L\). This constructs a sharp false positive, and proves the universal certification assertion in part 3. \(\square\)

**Small sharp boundary.** Over \(\mathbb F_2\) at \(N=2\),
\[
P_{2,2}(t)=(t+1)^2(t^2+t+1)=t^4+t^3+t+1.
\]
The sharp lift is \(g=x^2+x+y+y^2\). The theorem gives \(\operatorname{rank}g(X,Y)\le 2\operatorname{rank}(XY-I_m)\) at sizes \(m\le2\). At size \(3\), choose
\[
X=\begin{pmatrix}0&0&1\\1&0&1\\0&1&0\end{pmatrix},\qquad Y=X^{-1}.
\]
Direct computation gives
\[
Y=\begin{pmatrix}1&1&0\\0&0&1\\1&0&0\end{pmatrix},\qquad
g(X,Y)=\begin{pmatrix}0&1&0\\0&1&1\\1&0&1\end{pmatrix}\ne0.
\]
The matrix \(X\) has irreducible minimal polynomial \(t^3+t+1\), which does not divide \(P_{2,2}\); in particular \(XY-I_3=0\). This shows the bound really is sharp at the first nontrivial binary finite-size cutoff.

## Verification

Run `python3 verify.py` with Python 3; it uses only standard-library modules. The verifier constructs \(P_{q,N}\) from irreducibles and separately enumerates invertible matrices, testing the canonical annihilator and the sharp Laurent lift for \((q,N)=(2,1),(2,2),(3,1),(3,2)\). It checks the next-size counterexample for each of those four cases; for \((2,2)\) and \((3,2)\), it also checks the actual rank inequality over **all** square matrix pairs through size two, amounting to 260 and 6570 pairs respectively. It verifies \(D_{2,3}=11\) and the displayed explicit binary witness.

The program ends with `VERIFY_OK`. These finite experiments confirm illustrative cases and the arithmetic used in the examples; the general theorem for all prime powers and all sizes is proved in the preceding steps, not inferred from enumeration.

## Relationship to prior work

Yan and Yang [1] prove the homogeneous case of a proposed rank Nullstellensatz and give the pair \(xy-1\), \(yx-1\) as a nonhomogeneous obstruction over an algebraically closed characteristic-zero field. Their Proposition 3.1 supplies the equal-rank observation used in Step 3; it does not classify other polynomials, finite fields, bounded tests, or least false-positive word degree. Shamovich and Volčič [2] characterize **equality** of matrix-evaluation ranks by stable association in the algebraically closed characteristic-zero setting. That is a different quantifier and ground field from the present finite-field *inequality* filtration. Klep, Vinnikov, and Volčič [3] study vanishing ideals and give size bounds for rational identities in a different, infinite-field setting; their Theorem 3.8 does not state the finite-field annihilator \(P_{q,N}\) nor the sharp rank-domination cutoff. Draisma, Kahle, and Wiersig [4] bound sparsity of commutative polynomials vanishing on bounded-rank generic matrices; the object and minimization measure differ from the present inverse-pair and word-degree problem.

The formula for \(P_{q,N}\) invokes standard rational canonical form and classical finite-field irreducible counts, not a newly claimed classification of those individual ingredients. The contribution here is their **exact combination** with rank domination for an infinite family of finite-field truncations and a sharp degree threshold for *all* candidate free polynomials.

## Limitations

The cutoff formula is specific to the one-sided inverse relation \(xy-1\) and the finite coefficient field. It is not a theorem for arbitrary nonhomogeneous generators. Testing only a finite list of dimensions is not by itself a certificate for unlimited polynomial degree: the exhibited sharp false positives show why the degree hypothesis matters. Earlier literature could contain an equivalent formulation using polynomial identities of finite general linear groups; the comparisons made here do not exclude every such historical source.

## References

[1] Sizhuo Yan and Jianting Yang, *On a Rank Nullstellensatz Conjecture for Noncommutative Polynomials*, arXiv:2610.01804v1 (first publicly available 2026-10-01), https://arxiv.org/html/2610.01804v1 .

[2] Eli Shamovich and Jurij Volčič, *Global structure behind pointwise equivalences of noncommutative polynomials*, arXiv:2505.07469v1 (2025), https://arxiv.org/html/2505.07469v1 .

[3] Igor Klep, Victor Vinnikov, and Jurij Volčič, *Null- and Positivstellensätze for rationally resolvable ideals*, Linear Algebra Appl. **527** (2017), 260–293; arXiv:1504.08004v2, https://arxiv.org/html/1504.08004v2 .

[4] Jan Draisma, Thomas Kahle, and Finn Wiersig, *No short polynomials vanish on bounded rank matrices*, Bull. London Math. Soc. **55** (2023), 1791–1807, DOI:10.1112/blms.12819, https://doi.org/10.1112/blms.12819 .
