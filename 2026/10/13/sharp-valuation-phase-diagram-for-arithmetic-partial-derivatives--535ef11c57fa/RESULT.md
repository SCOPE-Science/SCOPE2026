# Sharp valuation phase diagram for arithmetic partial derivatives
## Finding
Fix a prime \(p\). For integers, define \(D_p(0)=0\) and
\[
D_p(n)=rac{n
u_p(n)}p\qquad(n
e0).
\]
Write a nonzero integer as \(n=a p^e\), where \(p
mid a\) and \(e\ge0\). Then the orbit is determined exactly by \(e\):

If \(0\le e<p\), then for every \(0\le j\le e\),
\[
D_p^{(j)}(n)=arac{e!}{(e-j)!}p^{e-j},
\]
and \(D_p^{(e+1)}(n)=0\).

If \(p\le e\le2p-1\), then the same formula holds for \(0\le j\le e-p\), and
\[
D_p^{(e-p)}(n)=arac{e!}{p!}p^p
\]
is fixed by \(D_p\).

If \(e\ge2p\), then for every \(j\ge0\),
\[
\left|D_p^{(j)}(n)ight|\ge2^j|n|,
\]
so the orbit diverges in absolute value.

Consequently the extinction basin is exactly \(0\le
u_p(n)<p\), the nonzero fixed-point basin is exactly \(p\le
u_p(n)\le2p-1\), and the divergent basin is exactly \(
u_p(n)\ge2p\). The thresholds are sharp. Every nonzero periodic integer is already fixed, and the nonzero fixed points are precisely \(a p^p\) with \(p
mid a\).

## Assumptions and scope
The statement concerns the arithmetic partial derivative on integers for one fixed prime \(p\). The coefficient \(a\) may be positive or negative. The claim does not concern the full arithmetic derivative, arithmetic subderivatives with more than one prime, or arbitrary elements of a \(p\)-adic field.

## Proof
For a nonzero integer \(x=b p^m\) with \(p
mid b\),
\[
D_p(x)=b m p^{m-1},
\]
so
\[

u_p(D_p(x))=m-1+
u_p(m).
\]

Suppose first that \(1\le m<p\). Then \(p
mid m\), hence the next valuation is \(m-1\), and the \(p\)-free coefficient is multiplied by \(m\). Iterating gives
\[
D_p^{(j)}(a p^e)=arac{e!}{(e-j)!}p^{e-j}
\]
for \(0\le j\le e\). At \(j=e\) the value is \(a e!\), which is prime to \(p\), so one more partial derivative is zero. The case \(e=0\) is immediate from the definition.

Now suppose \(p\le e\le2p-1\). For every integer \(m\) with \(p<m<2p\), one has \(p
mid m\), so each step lowers the valuation by one and multiplies the \(p\)-free coefficient by the current valuation. After exactly \(e-p\) steps the valuation is \(p\), giving
\[
D_p^{(e-p)}(a p^e)=arac{e!}{p!}p^p.
\]
The coefficient \(a e!/p!\) is prime to \(p\), because all factors \(p+1,\ldots,e\) are prime to \(p\). Since \(D_p(c p^p)=c p^p\) whenever \(p
mid c\), the orbit is then fixed.

Finally suppose \(m\ge2p\). If \(m>2p\), then
\[
m-1+
u_p(m)\ge m-1\ge2p.
\]
At the boundary \(m=2p\), the next valuation is again at least \(2p\): it equals \(2p\) for odd \(p\), while for \(p=2\) it equals \(5\). Thus the region \(m\ge2p\) is forward invariant. At every step in that region,
\[
rac{|D_p(x)|}{|x|}=rac m p\ge2.
\]
Induction gives \(|D_p^{(j)}(n)|\ge2^j|n|\), proving divergence. The boundary examples \(e=p-1,p,2p-1,2p\) show that both thresholds are sharp.

## Verification
The accompanying checker evaluates the exact formulas and boundary behavior for every prime \(p\le97\), six signed \(p\)-free coefficients, every exponent below \(2p\), and sampled divergent exponents from \(2p\) through \(2p+30\). It also verifies forty successive doubling inequalities in each sampled divergent orbit. The run completed with `VERIFY_OK` after 786314 assertions.

The computation is a regression check only; the infinite statement is proved by the valuation argument above.

## Relationship to prior work
Emmons and Xiao define \(D_p\), prove eventual periodicity of the valuation sequence, and prove a trichotomy in which integer orbits eventually become zero, eventually become a fixed point of the form \(a p^p\), or diverge in absolute value. Their theorem does not state an exact criterion in terms of the initial valuation, exact extinction or landing times, the fixed value reached from the middle band, or the quantitative lower bound \(2^j|n|\) in the divergent band.

Their later extension to \(p\)-adic fields gives a broader description of valuation dynamics in a non-Archimedean setting. That work likewise does not state the sharp integer thresholds \(p\) and \(2p\), because its focus is the valuation sequence over local fields rather than this Archimedean phase diagram for integer magnitudes.

## Limitations
The result is specific to a single-prime arithmetic partial derivative. It does not resolve the much harder dynamics of the full arithmetic derivative, where new prime factors can appear, and it does not classify multi-prime arithmetic subderivatives. The originality comparison is limited by ordinary literature-index coverage; an unindexed observation could conceivably contain the same elementary threshold reduction.

## References
1. Brad Emmons and Xiao Xiao, *The Arithmetic Partial Derivative*, Journal of Integer Sequences 25 (2022), Article 22.4.7; arXiv:2201.12453.
2. Brad Emmons and Xiao Xiao, *A generalization of arithmetic derivative to p-adic fields and number fields*, Notes on Number Theory and Discrete Mathematics 30 (2024), 357–382, DOI:10.7546/nntdm.2024.30.2.357-382.
