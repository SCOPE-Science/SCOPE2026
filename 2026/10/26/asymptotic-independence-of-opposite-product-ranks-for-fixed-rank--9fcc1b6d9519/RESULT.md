# Asymptotic independence of opposite product ranks for fixed-rank finite-field idempotents

## Finding
Fix a prime power \(q\ge2\) and positive integers \(r,s\). For each \(n\ge r+s\), choose independently and uniformly rank-\(r\) and rank-\(s\) idempotent matrices \(E,F\in M_n(\mathbb F_q)\). Let \(R=\operatorname{rank}(EF)\) and \(S=\operatorname{rank}(FE)\). Let \(p_{r,s,q}(t)\) be the rank distribution of a uniformly random \(r\times s\) matrix:
\[
p_{r,s,q}(t)=q^{-rs}{r\brack t}_q\prod_{i=0}^{t-1}(q^s-q^i),\qquad 0\le t\le\min(r,s).
\]
Then the joint law of \((R,S)\) is within total variation distance \(\delta_{n,r,s,q}\) of the product of two copies of \(p_{r,s,q}\), where
\[
\delta_{n,r,s,q}=1-\frac{\prod_{i=0}^{s-1}(1-q^{i-(n-r)})}{\prod_{i=0}^{s-1}(1-q^{i-n})}.
\]
In particular, \((R,S)\) converges in distribution, as \(n\to\infty\) with \(q,r,s\) fixed, to independent and identically distributed finite-field matrix ranks. The bound tends to zero at rate \(O_{q,r,s}(q^{-(n-r-s+1)})\).

The noncommutative asymmetry is genuine: when \(r=s=1\), its exact probability is
\[
\Pr(R\ne S)=2(1-q^{-1})\frac{q^{n-1}-1}{q^n-1}\longrightarrow \frac{2(q-1)}{q^2}.
\]

## Assumptions and scope
An idempotent means \(E^2=E\) over \(\mathbb F_q\), without any adjoint/self-adjoint requirement. The matrix-rank conditional sampling is uniform over each idempotent rank class. Composition order is standard matrix multiplication. Total variation distance is half the sum of absolute point-mass differences. The result holds for every fixed prime-power field size and all positive ranks, once \(n\ge r+s\). The rank law is zero outside \(0\le t\le\min(r,s)\).

## Proof
**1. Conjugation normalization.** Every rank-\(r\) idempotent is conjugate to \(\operatorname{diag}(I_r,0)\). Because the independently sampled rank-\(s\) idempotent is invariant under conjugation, fixing \(E=\operatorname{diag}(I_r,0)\) does not change the joint distribution of the two ranks.

**2. A uniform frame--coframe model.** Write \(F=UB\), where \(U\) is an \(n\times s\) column frame, \(B\) is an \(s\times n\) matrix, and \(BU=I_s\). Every rank-\(s\) idempotent has exactly \(|\mathrm{GL}_s(\mathbb F_q)|\) such representations (change of image basis), so uniform choice among these representations produces uniform \(F\). Conversely, choosing \(B\) uniformly among full-row-rank \(s\times n\) matrices, and then choosing \(U\) uniformly among its right inverses, gives that representation measure: each surjective \(B\) has exactly \(q^{s(n-s)}\) right inverses.

Write \(m=n-r\), split \(U=\binom A{U_0}\) into \(A\in M_{r\times s}(\mathbb F_q)\) and \(U_0\in M_{m\times s}(\mathbb F_q)\), and split \(B=(C\ B_0)\) with \(C\in M_{s\times r}(\mathbb F_q)\) and \(B_0\in M_{s\times m}(\mathbb F_q)\). The condition becomes \(CA+B_0U_0=I_s\). Since \(B\) is surjective and \(U\) injective, \(\operatorname{rank}(EF)=\operatorname{rank}(A)\), and \(\operatorname{rank}(FE)=\operatorname{rank}(C)\).

**3. Exact conditional independence.** Consider the event \(G\) that \(B_0\) has full row rank. Conditional on \(G\), the matrices \(B_0\) and \(C\) are respectively uniform among full-row-rank \(s\times m\) matrices and all \(s\times r\) matrices; in particular \(C\) is uniform. For every fixed \((B_0,C,A)\), exactly \(q^{s(m-s)}\) matrices \(U_0\) solve \(B_0U_0=I_s-CA\), because each of the \(s\) columns has an affine solution space of dimension \(m-s\). Thus \(A\) is uniform independently of \(C\), conditional on \(G\). In this event the two product ranks have exactly the independent uniform rectangular-matrix rank laws.

**4. Quantitative probability of the event.** For a uniformly random \(s\times k\) matrix the probability of full row rank is \(\prod_{i=0}^{s-1}(1-q^{i-k})\) for \(k\ge s\). Since \(B_0\) full row rank implies \(B\) full row rank, conditioning on full rank of \(B\) yields
\[
\Pr(G)=\frac{\prod_{i=0}^{s-1}(1-q^{i-m})}{\prod_{i=0}^{s-1}(1-q^{i-n})}.
\]
The unconditional joint rank law is a mixture of the claimed independent law (weight \(\Pr(G)\)) and a second law. Hence its total variation distance from the independent law is at most \(1-\Pr(G)=\delta_{n,r,s,q}\). Moreover, using \(1-\prod_i(1-x_i)\le\sum_i x_i\),
\[
\delta_{n,r,s,q}\le\frac{q^{-(n-r)}\sum_{i=0}^{s-1}q^i}{\prod_{j=1}^{s}(1-q^{-j})},
\]
which proves the stated geometric rate. The product rank formula is the number of rank-\(t\) \(r\times s\) matrices divided by \(q^{rs}\): first choose the \(t\)-dimensional image, then a surjection from \(\mathbb F_q^s\) to that image.

**5. Exact rank-one asymmetry.** Fix \(r=s=1\) and write \(E=u\alpha\) with \(\alpha(u)=1\) and \(F=v\beta\) with \(\beta(v)=1\). Then \(EF=0\) precisely when the image line of \(F\) lies in \(\ker\alpha\), an event of probability \((q^{n-1}-1)/(q^n-1)\). Given this line, it is distinct from the line of \(E\), and the proportion of complementary kernel choices satisfying \(\beta(u)=0\) is \(1/q\). Thus \(\Pr(EF=0,FE\ne0)=(1-q^{-1})(q^{n-1}-1)/(q^n-1)\). Reversing \(E,F\) gives the same probability. The two events are disjoint, proving the stated formula.

## Verification
`check.py` independently constructs binary-field rank-\(s\) idempotent matrices using all possible right-inverse presentations, deduplicates their matrix entries, checks idempotence by literal multiplication, and calculates the two ordered product ranks from the actual matrix. It checks all joint frequencies for seven \((n,r,s)\) settings with \(n\le5\), including a total of 21,050 idempotent matrices across configurations. It independently enumerates rectangular matrices to obtain the proposed product-limit law and checks the exact finite-dimensional total-variation inequality using rational arithmetic. Execute `python3 check.py` (Python standard library only). The file `check_output.txt` records the tested cases and final status. This finite computation is corroboration, not a proof of convergence.

## Relationship to prior work
Steinberg's study of the finite full matrix monoid and its idempotent rank classes gives the semigroup framework and rank stratification, but studies semigroup determinants, not paired random idempotent product-rank laws. Koenig and Nguyen's rank-universality results include the rank of corners of uniform invertible matrices, but do not give independence of the two *opposite* product-rank statistics under the shared idempotent constraint. Perret-Gentil studies matrices and inverses as the *field size grows in fixed dimension*, a different limit regime. None of these inspected statements implies the present joint-rank law without additional arguments connecting the coupled frame--coframe blocks.

## Limitations
The ranks \(r,s\) and field size \(q\) are fixed as ambient dimension grows. A growing-rank regime is not proved. The explicit total-variation bound need not be sharp; the proof does not give an exact finite-dimensional joint distribution except in the rank-one example. Computational checks were over \(\mathbb F_2\), while the proof covers every prime power. The originality assessment is based on accessible literature and database comparisons, not an exhaustive uniqueness theorem; an equivalent implicit result in unsurveyed matrix-enumeration literature remains possible. No independent mathematical audit has been performed.

## References
- B. Steinberg, *Factoring the Dedekind-Frobenius determinant of a semigroup*, arXiv:2108.02166v1, first posted 2021-08-04; especially Section 4, https://arxiv.org/html/2108.02166v1.
- J. Koenig and H. Nguyen, *Rank of Near Uniform Matrices*, arXiv:2101.00107v1, first posted 2020-12-31; especially Theorem 1.16 and its proof, https://arxiv.org/abs/2101.00107.
- C. Perret-Gentil, *Joint distribution of inverses in matrix groups over finite fields*, arXiv:1810.11422v1, first posted 2018-10-26, https://arxiv.org/abs/1810.11422.
