# Review

## Scientific claim reviewed

The stabilized obstruction set for sums of exactly j positive tenth powers is the positive gap set of the numerical semigroup

\[
\Gamma_{10}=\langle1023,59048,25937424600\rangle,
\]

with Frobenius number \(259379677393\) and genus \(129689838697\). Consequently the exponent-10 cases of the Benfield--Lippard even-exponent symmetry relations hold.

## Correctness

**PASS.** The proof reduces the Waring-offset problem to an additive-semigroup gap problem and then determines that semigroup exactly.

For an offset \(b\), subtracting the baseline contribution of \(j\) copies of \(1^{10}\) shows that \(j+b\) is a sum of exactly \(j\) positive tenth powers exactly when \(b\) is a sum of at most \(j\) generators \(m^{10}-1\). Thus the stabilized offsets are precisely the positive gaps of \(\Gamma_{10}\).

The infinite generating family collapses to three generators. For \(11\nmid m\), Fermat's little theorem makes \((m^{10}-1)/11\) integral. The only cases below the Frobenius number of \(T=\langle93,5368\rangle\) are handled explicitly; every \(m\ge5\) has quotient above \(F(T)=493763\). For \(11\mid m\), the generator is either \(C=11^{10}-1\) or differs from \(C\) by 11 times an integer larger than \(F(T)\). This proves
\[
\Gamma_{10}=11T+C\mathbb Z_{\ge0}.
\]

Because \(C\in T\) and \(C\equiv-1\pmod{11}\), every residue class has a canonical form \(rC+11z\), and membership in \(\Gamma_{10}\) is equivalent to \(z\in T\). Sylvester's formulas for \(T\), followed by an exact residue-class count, yield
\[
F(\Gamma_{10})=259379677393,\qquad
g(\Gamma_{10})=129689838697.
\]
Their relation \(F=2g-1\) and the explicit residue correspondence establish symmetry.

The standalone verifier independently enumerates \(T\) through its Frobenius number, checks the stated genus and symmetry, verifies the small exceptional reductions and an explicit expression of \(C\) in \(T\), checks original generators for \(1\le m\le500\), and reproduces all final constants. These computations agree with the symbolic proof and are not used in place of it.

## Originality

**PASS, to the best of our knowledge.** Benfield--Lippard's current arXiv version (v2, revised 31 March 2025) computes the stable sets through exponent 9, states the even-exponent symmetry conjectures, and gives only the lower bound
\[
|\mathbf B^{10}|\ge129687123005
\]
in Corollary 10.8.

Searches covered the exact values \(259379677393\) and \(129689838697\), the semigroup generators \(1023,59048,25937424600\), the equivalent forms \(2^{10}-1,3^{10}-1,11^{10}-1\), `B^10`, numerical-semigroup formulations of the positive-power problem, the source-paper title, and recent follow-up/citation queries. No source located the exact exponent-10 determination or an equivalent three-generator reduction.

Zenkin's 1995 *The generalized Waring problem: A new property of positive integers* is a relevant older source underlying the generalized-Waring framework. Its abstract and bibliographic record were inspected, but its subscription-only full text was not. The later Benfield--Lippard paper cites Zenkin while still presenting the tenth-power result only as a lower bound. Nevertheless, this unavailable full text is the principal residual literature risk. The general offset-semigroup reformulation is therefore not claimed as new; the originality claim is restricted to the exact exponent-10 semigroup collapse, Frobenius/genus values, and resulting exponent-10 symmetry result.

## Value

**PASS.** The result converts a published lower bound of roughly \(1.3\times10^{11}\) stable obstructions into an exact description of the entire obstruction set via three generators, computes both principal invariants in closed form, and verifies two structural conjectures at the first exponent beyond the paper's computed range. The proof is finite and conceptual rather than an enumeration of the obstruction set.

## Review status

Same-model review: passed. Independent audit: not yet performed.
