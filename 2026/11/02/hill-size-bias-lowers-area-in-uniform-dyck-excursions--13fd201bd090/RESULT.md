# Hill-size bias lowers area in uniform Dyck excursions

## Finding

**Theorem (finite-size hill–area transport).** For every integer \(n\ge1\), let \(P\) be uniform on the set \(\mathcal D_n\) of Dyck words with \(n\) up-steps and \(n\) down-steps. A *hill* is a consecutive \(UD\) pair beginning at height zero; \(H(P)\) is the number of hills. Define area by
\[
A(P)=\sum_{\text{up-steps }u}\operatorname{height}_{\mathrm{before}}(u).
\]
Write \(C_n=\frac1{n+1}\binom{2n}{n}\). The hill-size-biased law is \(\Pr(P^\star=p)=H(p)/C_n\); it is normalized because \(\mathbb EH=1\).

There is a coupling with
\[
A(P)-A(P^\star)=J\ge0,\qquad
\Pr(J=j)=\frac{C_jC_{n-1-j}}{C_n}\quad(0\le j\le n-1).
\]
Consequently, for **every nondecreasing** function \(f\) on the attainable finite area set,
\[
\operatorname{Cov}(H,f(A))\le0,
\]
strictly for all strictly increasing \(f\) if \(n\ge2\). In particular,
\[
\boxed{\operatorname{Cov}(H,A)=-(n-1)/2}\qquad(n\ge1).
\]
The coupling identifies a stochastic domination of the *entire* area distribution, not only one negative covariance.

## Assumptions and scope

Dyck words are finite words on \(U,D\) with equal totals and every prefix having at least as many \(U\) as \(D\). Their semilength is \(n\). The area convention counts the altitude before each up-step; in the north-east/east Catalan lattice convention it equals the number of whole unit squares between the path and diagonal. The empty path has area zero. The uniformly random law assigns mass \(1/C_n\) to each word. Hill-size bias assigns total weight proportional to \(H\); we do not condition on \(H>0\) uniformly. This distinction is essential. Throughout \(n\ge1\).

In the standard depth-first bijection with rooted ordered plane trees with \(n\) edges, \(H\) counts leaf children of the root, while \(A=\sum_{v\ne\mathrm{root}}(\operatorname{depth}(v)-1)\). Thus the result concerns dependence between a local root configuration and global total path length.

## Proof

**1. A common Catalan pair space.** Let
\[
\mathcal Q_n=\coprod_{j=0}^{n-1}\mathcal D_j\times\mathcal D_{n-1-j}.
\]
The first-return decomposition \(U B D C\) is unique for any nonempty Dyck word. Hence \(|\mathcal Q_n|=\sum_{j=0}^{n-1}C_jC_{n-1-j}=C_n\). Uniform \((B,C)\in\mathcal Q_n\) therefore produces a uniform ordinary word \(P=UBDC\).

**2. A distinct, marked-hill bijection.** Send the same pair to \((P^\star,h)=(BUDC,\text{the displayed }UD\text{ hill})\). The displayed pair begins at altitude zero because \(B\) is itself a complete Dyck path. Conversely, deleting an arbitrary distinguished hill from a Dyck word yields the unique prefix \(B\) and suffix \(C\), each a complete Dyck word. Thus the correspondence is a bijection of \(\mathcal Q_n\) with all Dyck paths of semilength \(n\) equipped with a marked hill. Consequently the number of marked paths is exactly \(C_n\), \(\sum_{p\in\mathcal D_n}H(p)=C_n\), and the unmarked law of \(P^\star\) is \(H(p)/C_n\).

**3. The deterministic area drop.** If \(|B|=j\) up-steps, then every up-step inside \(B\) is lifted by exactly one unit in \(U B D C\), whereas \(C\) remains at ground level. Thus
\[
A(UBDC)=A(B)+A(C)+j,
\qquad A(BUDC)=A(B)+A(C).
\]
Set \(J=j\). There are \(C_jC_{n-1-j}\) pairs with this \(j\), proving both the area coupling and the stated exact law of \(J\). For \(n\ge2\), positive probability lies on \(J\ge1\), so every strictly increasing \(f\) has \(\mathbb Ef(A(P^\star))<\mathbb Ef(A(P))\). For any nondecreasing \(f\), the analogous inequality is weak.

**4. Covariance and its exact size.** From \(\mathbb EH=1\), for every \(f\),
\[
\mathbb Ef(A(P^\star))=\mathbb E[Hf(A)],
\quad
\operatorname{Cov}(H,f(A))=
\mathbb E[f(A(P^\star))-f(A(P))].
\]
The map \((B,C)\mapsto(C,B)\) preserves the uniform pair space and swaps \(J\) with \(n-1-J\). Therefore \(\mathbb EJ=(n-1)/2\), and using \(f(t)=t\) gives \(\operatorname{Cov}(H,A)=-(n-1)/2\). The formula remains valid at \(n=1\) when \(J=0\).

**5. Weighted refinements.** Defining \(C_j(q)=\sum_{R\in\mathcal D_j}q^{A(R)}\), the two bijections and their area formulas yield, as polynomial identities in an indeterminate \(q\),
\[
C_n(q)=\sum_{i+j=n-1}q^iC_i(q)C_j(q),
\qquad
\sum_{p\in\mathcal D_n}H(p)q^{A(p)}=\sum_{i+j=n-1}C_i(q)C_j(q).
\]
These identities provide another reproducible check of the transport theorem, but the stochastic assertion follows directly from the explicit coupling.

## Verification

The standalone script `verify_hills_area.py` uses Python's standard library, independently enumerates every Dyck word for \(1\le n\le10\), and compares (i) Catalan totals; (ii) total hill and area moments; (iii) the marked-hill area distribution with the pair-space construction; (iv) the coupling shift and its mean; and (v) every integer-threshold stochastic tail inequality. Running `python verify_hills_area.py` returned `PASS: 23957 exact assertions`. All operations are integral, with no floating-point tolerance. The finite checks corroborate rather than establish the statement for unbounded \(n\), which is proved bijectively above.

## Relationship to prior work

Peart and Woan (2001) count Dyck paths avoiding peaks at specified heights, and Elizalde and Deutsch (2003) study bijections and statistics involving hills. Cameron and McLeod (2016) study returns and the parity of hill counts. These establish the marginal importance of the height-one peak statistic. Haug and Prellberg (2014) study the area-weighted Catalan recursion; Kargin (2024) treats area jointly with the **total number of peaks**, which differs from the ground-level hill count. The new claim is the explicit *hill-size-biased versus uniform* area coupling, its all-increasing-functions stochastic sign, and its exact covariance. It does not assert novelty of Catalan first-return decompositions, marginal hill counting, or marginal \(q\)-area formulas.

## Limitations

The result applies to uniform Dyck paths only and to the explicitly normalized area statistic. A different weighting of paths or an arbitrary peak-height statistic is not covered. The size-biased word \(P^\star\) can have no unique unmarked hill position; the mark is part of the construction, not the law being compared. No independence between \(J\) and the lower area \(A(P^\star)\) is asserted. The proof is self-contained but the historical-priority comparison is incomplete: the full text of Pergola's 2001 paper on area bijections was inaccessible, and broader classical enumerations could imply the reported identities in another formulation. Independent historical review has not been performed.

## References

1. P. Peart and W.-J. Woan, *Dyck Paths With No Peaks At Height k*, Journal of Integer Sequences 4 (2001), Article 01.1.3. https://cs.uwaterloo.ca/journals/JIS/VOL4/PEART/pwatjis2.pdf (published 2001-05-12).
2. S. Elizalde and E. Deutsch, *A simple and unusual bijection for Dyck paths and its consequences*, arXiv:math/0306125v1 (2003-06-09). https://arxiv.org/pdf/math/0306125
3. N. Haug and T. Prellberg, *Uniform asymptotics of area-weighted Dyck paths*, arXiv:1412.5108v1 (2014-12-16). https://arxiv.org/pdf/1412.5108
4. N. T. Cameron and J. E. McLeod, *Returns and Hills on Generalized Dyck Paths*, Journal of Integer Sequences 19 (2016), Article 16.6.1. https://cs.uwaterloo.ca/journals/JIS/VOL19/McLeod/mcleod3.pdf
5. V. Kargin, *On the joint distribution of the area and the number of peaks for Bernoulli excursions*, arXiv:2412.20315v1 (2024-12-29). https://arxiv.org/pdf/2412.20315
6. E. Pergola, *Two bijections for the area of Dyck paths*, Discrete Mathematics 241 (2001), 435–447. https://doi.org/10.1016/S0012-365X(01)00129-7 (comparison incomplete: full text not inspected).
