# Antithetic coupling rigidity and logarithmic stiff damping for randomized implicit stages

## Finding

Consider the uniform-random implicit stage factor \(R_z(u)=(1+(1-u)z)/(1-uz)\), where \(u\in[0,1]\). Couple two successive stage choices \((U,V)\) while preserving the uniform distribution of each component. Among **all** joint distributions with these marginals, the **only** coupling with samplewise unconditional stability \(|R_{-s}(U)R_{-s}(V)|\le 1\) almost surely for each \(s>0\) is \(V=1-U\) almost surely. This coupling also gives samplewise Euclidean nonexpansiveness for **every dissipative complex matrix**, not just scalar negative eigenvalues.

For \(U\sim\mathrm{Unif}(0,1)\), the antithetic pair has scalar transfer
\[
P_z(U)=\frac{1+z+U(1-U)z^2}{1-z+U(1-U)z^2}.
\]
Its exact mean-square contraction gap on \(z=-s\), for \(s>0\), is
\[
\delta(s)=1-\mathbb E\bigl[|P_{-s}(U)|^2\bigr]
=\frac{8(s^2+2s+4)\log(1+s)}{(s+2)^3}
-\frac{8s^2}{(s+2)^2(s+1)},
\]
and obeys the sharp stiff-step law
\[
\delta(s)=\frac{8\log s-8+o(1)}s\quad(s\to\infty).
\]
Thus uniform-marginal antithetic pairing uniquely restores samplewise unconditional stability but does not give uniform stiff decay: the mean-square damping gap tends to zero.

## Assumptions and scope

The object is the autonomous linear test problem \(y'=Ay\) under two consecutive steps of equal length \(h>0\), with the random implicit stage factor \(R_{hA}(u)=(I+(1-u)hA)(I-uhA)^{-1}\). This is the linear autonomous specialization of the randomized implicit two-stage methods described in Bochacik–Przybyłowicz (2024); here the random stage choices across successive steps are **coupled**, rather than independent as in their algorithm. The coupled extension is explicitly a different sampling rule. Let \((U,V)\) have arbitrary joint law on \([0,1]^2\) with both marginals uniform. Samplewise scalar unconditional stability means that for each \(s>0\) the product at \(z=-s\) has modulus at most one outside a null event that may depend on \(s\). The matrix assertion applies to every finite-dimensional complex matrix \(A\) satisfying \(A+A^*\preceq0\). The moment formula assumes the unique antithetic coupling \(V=1-U\).

## Proof

**1. Rigidity of the coupling.** Since uniform variables lie in \((0,1)\) almost surely, for each such sample
\[
\lim_{n\to\infty}|R_{-n}(U)R_{-n}(V)|
=\frac{(1-U)(1-V)}{UV}.
\]
If the product is contractive almost surely for every positive integer \(n\), the countable intersection of these probability-one events has probability one. Its limit then implies \((1-U)(1-V)\le UV\), or \(U+V\ge1\), almost surely. Uniform marginals give \(\mathbb E(U+V)=1\). Therefore the nonnegative integrable variable \(U+V-1\) must vanish almost surely, so \(V=1-U\). This proves necessity without any independence assumption or exceptional-value ambiguity.

**2. Transfer identity.** For \(v=1-u\), multiply the rational step factors and put \(c=u(1-u)\):
\[
R_z(u)R_z(1-u)=\frac{(1+uz)(1+(1-u)z)}{(1-uz)(1-(1-u)z)}
=\frac{1+z+cz^2}{1-z+cz^2}.
\]
For a scalar \(z\) with \(\Re z\le0\), the denominators cannot vanish; the exact difference of squared moduli is
\[
|1-z+cz^2|^2-|1+z+cz^2|^2
=-4(1+c|z|^2)\Re z\ge0.
\]
This proves scalar contractivity, strictly for \(\Re z<0\), and completes sufficiency of antithetic pairing for the scalar condition in step 1.

**3. Nonnormal dissipative matrices.** Fix \(c=u(1-u)\) and \(B=hA\). Set \(D=I-B+cB^2=(I-uB)(I-(1-u)B)\) and \(N=I+B+cB^2\). Dissipativity makes both linear factors of \(D\) invertible. For any vector \(y\), the polarization identity gives
\[
\|Dy\|_2^2-\|Ny\|_2^2
=-4\Re\langle(I+cB^2)y,By\rangle
=-4\bigl(\Re\langle y,By\rangle+c\Re\langle By,B(By)\rangle\bigr)\ge0.
\]
The last inequality applies the same matrix dissipativity inequality first to \(y\), then to \(By\). Therefore \(\|ND^{-1}\|_2\le1\), with no normality or diagonalizability assumption. Since all rational factors are functions of \(A\), \(ND^{-1}\) is the two-step matrix amplification. This also proves the pair is well-defined for all \(h>0\).

**4. Exact mean-square gap.** For \(z=-s\), put \(c=u(1-u)\) and \(D_s(u)=1+s+s^2c\). Then \(P_{-s}(u)=1-2s/D_s(u)\), and direct expansion gives
\[
\delta(s)=4s\int_0^1\frac{du}{D_s(u)}
-4s^2\int_0^1\frac{du}{D_s(u)^2}.
\]
Substitute \(u=(1+t)/2\). Elementary integrals, valid for all \(s>0\), yield
\[
I_1=\int_0^1\!D_s(u)^{-1}du=\frac{2\log(1+s)}{s(s+2)},
\]
\[
I_2=\int_0^1\!D_s(u)^{-2}du
=\frac{2}{(s+2)^2(s+1)}+\frac{2I_1}{(s+2)^2}.
\]
Substitution into \(4sI_1-4s^2I_2\) simplifies to the stated formula. Positivity for finite \(s>0\) also follows from the strict scalar contraction at \(-s\). Expanding the exact formula as \(s\to\infty\) gives \(s\delta(s)-8\log s\to-8\), which proves the claimed asymptotic.

**5. Consistency observation (not claimed as novel).** Expanding the transfer at \(z=0\) gives \(P_z(u)=1+2z+2z^2+O(z^3)\), which matches the exponential over two steps on autonomous linear problems. Symmetric/adjoint compositions and their familiar order cancellation are established in earlier composition-method literature.

## Verification

The standalone `verification.py` uses exact SymPy rational identities for the transfer, its first two derivatives, the closed mean-square gap, and the two-term asymptotic. High-precision quadrature checks the gap formula at seven positive values of \(s\). It additionally tests 1,680 randomly generated nonnormal dissipative matrix cases. The script prints a single `VERIFY_OK` status on success. These checks supplement, but do not replace, the analytical proof of the all-coupling and all-matrix assertions. Install packages listed in `requirements.txt` and run `python verification.py`.

## Relationship to prior work

Bochacik and Przybyłowicz, arXiv:2404.19059v1 (first public April 29, 2024), introduced and studied randomized implicit two-stage schemes with independent stage randomness and established stability results for that model; their formula provides the single-step transfer studied here. This result changes the between-step coupling while preserving each stage's uniform marginal. Standard deterministic adjoint-composition ideas already explain why complementary parameters yield a symmetric pair, so the order-two Taylor expansion is not advanced as an original discovery. The contribution assessed here is the **uniqueness of antithetic coupling among all uniform-marginal couplings under a samplewise all-step-size criterion**, the extension of the contractive pair to nonnormal dissipative matrices, and the **exact logarithmic stiff damping law**. These statements are not implied solely by independent-stage convergence or generic order statements; no claim of uniqueness of all possible stable integrators is made.

## Limitations

The uniqueness is relative to precisely defined two-stage products, equal step lengths, both stage marginals uniform, and **samplewise stability for all scalar negative-real step parameters**. Other couplings may be mean-square stable without satisfying this stronger pathwise criterion, and other numerical methods may be A-stable. The nonnormal proof covers finite-dimensional linear dissipative equations only, not general nonlinear B-stability, variable-step algorithms, or stochastic differential equations. The asymptotic gap describes one two-step block; it does not provide uniform stiff decay or an L-stability claim. This is a self-reviewed mathematical finding, not an independent audit or external certification.

## References

1. Bochacik and Przybyłowicz, *Convergence and stability of randomized implicit two-stage Runge–Kutta schemes*, arXiv:2404.19059v1 (2024), https://arxiv.org/abs/2404.19059.
2. Blanes, Casas, and Murua, *Splitting and composition methods in the numerical integration of differential equations*, arXiv:0812.0377 (2008), https://arxiv.org/abs/0812.0377. The adjoint-composition discussion provides the comparison for deterministic symmetrization and its order.
