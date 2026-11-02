# Triple-Poisson birthday transition for random generators of finite local-algebra powers

## Finding

Fix integers \(f,k\ge1\), \(0\le d\le k\), and a real constant \(c>0\). For each prime power \(q\), let \(R_q\) be **any** finite commutative unital \(\mathbb F_q\)-algebra that is local, has residue field \(\mathbb F_{q^f}\), and has cotangent dimension \(\dim_{\mathbb F_{q^f}}\mathfrak m_q/\mathfrak m_q^2=d\). Independently choose \(k\) uniform elements of
\[
A_q=R_q^{\,r_q},\qquad r_q=\lfloor c q^{fk/2}\rfloor.
\]
The following sharp *birthday-scale phase diagram* holds as \(q\to\infty\) over prime powers:
\[
\Pr\big(\text{the elements generate }A_q\text{ as a unital }\mathbb F_q\text{-algebra}\big)
\longrightarrow
\begin{cases}
0,&d>k/2+1,\\[2mm]
\exp\!\left(-\frac f2c^2-c\mathbf1_{2\mid f}-c\mathbf1_{2d=k+2}\right),&d\le k/2+1.
\end{cases}
\]
Here \(\mathbf1_E\) denotes the indicator of a stated condition. The limit is **independent of the multiplication and Loewy length** of the local factors beyond their residue degree and cotangent dimension.

More precisely, at the *triple-critical parameters* \(2\mid f\), \(2\mid k\), and \(d=k/2+1\), three obstruction counts converge jointly to **independent** Poisson random variables with respective means
\[
(c,\;c,\;fc^2/2).
\]
They count, respectively, residue tuples lying in a proper subfield, local cotangent matrices failing to span, and pairs of full-degree residue tuples lying in the same Frobenius orbit. Thus the generation probability tends to \(\exp(-2c-fc^2/2)\). The first case is \(f=k=d=2\), with limit \(\exp(-2c-c^2)\).

The phase diagram and joint Poisson law—not the pre-existing structural criterion for generating products of Artinian algebras—are the assessed finding.

## Assumptions and scope

All algebras are associative, commutative, unital, and finite-dimensional over the base finite field. A generating tuple always generates **as a unital algebra over \(\mathbb F_q\)**, not as a ring with a different base. The parameters \(f,k,d,c\) are fixed as \(q\to\infty\); the factors \(R_q\) may vary arbitrarily subject to the two invariants above. A local factor with \(d=0\) is its residue field. No assumption on the radical nilpotency exponent is made. The result does not concern noncommutative factors or families in which \(f,k,d\) also tend to infinity.

For a finite field extension of degree \(f\), define
\[
T_{q,f,k}=\sum_{e\mid f}\mu(e)q^{fk/e},\qquad H_{q,f,k}=T_{q,f,k}/f.
\]
Thus \(T_{q,f,k}\) counts vectors in \(\mathbb F_{q^f}^{\,k}\) having full Frobenius orbit length \(f\), and \(H_{q,f,k}\) counts the orbits. Let \(Q=q^f\).

For a uniform \(k\)-tuple in \(R_q^{r}\), let \(U\) be the number of coordinates whose residue vector has orbit length less than \(f\); \(V\) the number whose \(d\)-by-\(k\) cotangent coefficient matrix has rank less than \(d\); and \(W\) the number of unordered coordinate pairs whose two full-degree residue vectors share the same Frobenius orbit. These random variables are well-defined without choosing a presentation of \(R_q\); a coefficient-field identification only makes the tangent matrices explicit.

## Proof

**1. Exact finite counting reduction, from standard algebraic generation principles.** A finite local commutative \(\mathbb F_q\)-algebra has a canonical coefficient field isomorphic to \(\mathbb F_{q^f}\). To see this directly, set \(Q=q^f\). For any element \(x\), the difference \(x^Q-x\) is nilpotent because it vanishes in the residue field. Choosing \(N\) so large that every nilpotent has \(Q^N\)-th power zero gives \(x^{Q^{N+1}}=x^{Q^N}\); hence high iterates of \(Q\)-Frobenius provide a lift fixed by \(z^Q=z\) for every residue class. Such a lift is unique, since a nilpotent element fixed by \(Q\)-Frobenius must vanish. The fixed-point set is therefore the coefficient field. These powers also show that any subalgebra surjecting onto the residue field contains this coefficient field. By the nilpotent lifting lemma (cf. Kravchenko–Mazur–Petrenko, Proposition 2.5 and Corollary 2.6), a tuple generates one local factor if and only if its residue vector generates the residue field over \(\mathbb F_q\) and its images in \(\mathfrak m/\mathfrak m^2\) span that space over the coefficient field. The converse can also be proved by repeatedly replacing \(\mathfrak m\) by \(\mathfrak m^j\) in \(\mathfrak m=(B\cap\mathfrak m)+\mathfrak m^2\) for the generated subalgebra \(B\).

For \(r\) local factors with the same residue field, separate factors must have **different** Frobenius orbits of residue \(k\)-vectors. This is precisely the distinct-simple-quotient obstruction of Kravchenko–Mazur–Petrenko, Theorem 2.2. Equivalently, the residue polynomial maps from \(\mathbb F_q[t_1,\ldots,t_k]\) have distinct maximal kernels; Chinese remaindering gives all the residue idempotents, whose high Frobenius powers lift to actual orthogonal idempotents. Individual local surjectivity then implies generation of the product. Counting the \(r\) ordered full-degree vectors in different orbits gives \(\prod_{j=0}^{r-1}(T_{q,f,k}-fj)\). Independently, the probability that a uniform \(d\)-by-\(k\) matrix over \(\mathbb F_Q\) has full row rank is \(\prod_{j=0}^{d-1}(1-Q^{j-k})\). Therefore, when \(r\le H_{q,f,k}\) and \(d\le k\), the **exact finite-q identity** is
\[
\Pr(\mathrm{generate}\ R_q^r)=
\frac{\prod_{j=0}^{r-1}(T_{q,f,k}-fj)}{q^{fkr}}
\left(\prod_{j=0}^{d-1}(1-q^{f(j-k)})\right)^r.
\]
It is zero if \(r>H_{q,f,k}\) or \(d>k\). The empty matrix product is \(1\) if \(d=0\). This reduction uses established algebraic tools; it is included to fix normalization and prove the subsequent probabilistic statement self-containedly.

**2. The two independent single-coordinate obstructions.** For \(f\) even, the unique index-two subfield \(\mathbb F_{q^{f/2}}\) has the largest size of any proper subfield. Inclusion–exclusion on subfields gives
\[
\Pr(\text{residue not full degree})=q^{-fk/2}(1+o(1)).
\]
For odd \(f\) the same probability is \(o(q^{-fk/2})\) (and it is exactly zero when \(f=1\)). Since \(r_q\sim c q^{fk/2}\), the binomial count \(U_q\) tends to \(\operatorname{Pois}(c)\) for even \(f\), and tends in probability to zero for odd \(f\).

The probability of deficient cotangent rank is
\[
1-\prod_{j=0}^{d-1}(1-q^{f(j-k)})=
\begin{cases}0,&d=0,\\
q^{-f(k-d+1)}(1+o(1)),&1\le d\le k.
\end{cases}
\]
Its binomial count \(V_q\) therefore vanishes in probability if \(d<k/2+1\), converges to \(\operatorname{Pois}(c)\) if \(d=k/2+1\), and satisfies \(\Pr(V_q=0)\to0\) if \(d>k/2+1\). Cotangent coefficients and residues are independent in a uniform local-ring element, so \(V_q\) is independent of \((U_q,W_q)\) at every \(q\).

**3. Frobenius birthday collisions and joint independence.** Conditional on \(U_q=u\), the other \(r_q-u\) residue vectors select independent uniformly distributed orbits among \(H_{q,f,k}\sim q^{fk}/f\) orbits. Their collision count \(W_q\) has mean asymptotic to
\[
\frac{\binom{r_q}{2}}{H_{q,f,k}}\longrightarrow \frac f2c^2.
\]
To establish the entire law, use factorial moments. An ordered collection of \(j\) distinct pairs forms a graph on the sampled coordinates. The configurations of \(j\) disjoint pairs contribute \((fc^2/2)^j+o(1)\) to \(\mathbb E(W_q)_j\). Any configuration having a connected component with at least three vertices contributes \(o(1)\): a component with \(v\) vertices requires at least \(v-1\) independent orbit equalities, and its aggregate contribution is \(O(r_q^v/H_{q,f,k}^{v-1})=O(q^{fk(1-v/2)})\). Thus \(W_q\Rightarrow\operatorname{Pois}(fc^2/2)\). The argument is uniform for bounded \(u\), while \(U_q\) is tight; conditioning on \(U_q\) therefore proves the asymptotic independence of \(U_q\) and \(W_q\). Independence of \(V_q\) completes the joint limit when \(d\le k/2+1\).

**4. Phase diagram.** Generation is exactly \(U_q=V_q=W_q=0\), by Step 1. Taking zero probabilities of the independent limiting counts gives the displayed positive limit. In the remaining regime \(d>k/2+1\), the local rank obstruction alone forces probability to zero. Triple nonzero Poisson intensities require \(2\mid f\) and \(2d=k+2\), which in turn forces even \(k\). This proves both the classification and the triple-critical formula.

## Verification

A standalone direct-multiplication verifier, `verify.py`, constructs multiplication directly, obtains generated subalgebras by linear-span closure of words, and compares actual generation counts with the formula. It exhaustively checks ten \(\mathbb F_2\)- and \(\mathbb F_4\)-based square-zero local-power cases, two length-three truncation cases, and one mixed-cotangent-rank product of two nonisomorphic local algebras. These are finite checks, **not** proofs of the asymptotic statement. The general proof is in the four steps above.

For \(f=k=d=2\), \(c=1\), the exact probabilities for \(q=5,11,41,101\) are approximately \(0.04462225,0.04869621,0.04970812,0.04977405\); the proved limit is \(e^{-3}\approx0.04978707\). Values are reproducible by evaluating the finite product in Step 1 with logarithms. The exact two-generator cutoff is \(r\le(q^4-q^2)/2\) in this example, independently of nilpotency length.

## Relationship to prior work

Kravchenko, Mazur and Petrenko (2014, Section 2, especially Theorem 2.2 and Corollary 2.6) already prove the structural local-versus-residue and pairwise-simple-quotient reduction on which the finite product formula rests. Their results are *not* presented as new here. Their 2010 work develops random generation of finite algebras and treats matrix-algebra powers. Sercombe and Shalev (first preprint September 2, 2020) give random-generation bounds for general associative algebras; their emphasis differs from the birthday-scale family of increasingly many local factors. Arpin, Bozlee, Herr and Smith (2021) construct generator schemes and examine monogenic jets, without stating the Poisson three-obstruction window. The assessed additional statement is the **joint independent Poisson limit** and **complete critical phase diagram**, not algebraic generation criteria or mere factorial counting.

In the inspected published research records, the nearest thematic collision result concerns an ordered Boolean full product, not random algebra generators and cotangent-rank failures. No exact instance of this joint limit was located. An unlocated stronger general probabilistic generator-scheme theorem may still imply it; independent priority review is outstanding.

## Limitations

The probabilities assume uniformly independent random generators and a fixed number \(k\) of generators. The limit does not extend without further analysis to variable residue degrees or noncommutative local rings. The proof uses ordinary finite-field occupancy and standard nilpotent lifting; it supplies neither an optimal convergence rate nor a result for dynamically growing \(k\) or \(f\). The finite tests cover only small examples. Existing structural algebra-generation results are explicitly acknowledged, and no claim is made that the underlying exact local generation criterion originated here.

## References

1. R. V. Kravchenko, M. Mazur, B. V. Petrenko, *Generators of maximal orders*, arXiv:1406.6465 (June 25, 2014), especially Theorem 2.2 and Corollary 2.6; https://arxiv.org/abs/1406.6465.
2. D. Sercombe and A. Shalev, *Random generation of associative algebras*, arXiv:2009.01115 (first public September 2, 2020); https://arxiv.org/abs/2009.01115.
3. R. V. Kravchenko, M. Mazur, B. V. Petrenko, *On the smallest number of generators and the probability of generating an algebra*, arXiv:1001.2873 (2010); https://arxiv.org/abs/1001.2873.
4. S. Arpin, S. Bozlee, L. Herr and H. Smith, *The Scheme of Monogenic Generators I: Representability*, arXiv:2108.07185 (August 16, 2021); https://arxiv.org/abs/2108.07185.
