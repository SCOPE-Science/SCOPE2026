# Exact primitive two-cycle law for non-contingency on reflexive cyclic frames

## Finding

For every integer \(n\ge3\), the non-contingency operation \(\Delta\varphi:=\Box\varphi\lor\Box\neg\varphi\) on the reflexive symmetric cyclic Kripke frame with worlds \(\mathbb Z/n\mathbb Z\) and successor sets \(\{i-1,i,i+1\}\) has exactly one fixed valuation of a single propositional letter, namely the all-true valuation. Writing \(C_n\) for its number of unordered primitive two-cycles of valuations, the exact generating function is

\[
\sum_{n\ge3}C_nz^n=\frac{2z^4+5z^5+3z^6}{1-z^4-2z^5-z^6}.
\]

In particular, \(C_3,C_4,\ldots,C_{14}=0,2,5,3,0,2,9,15,11,5,13,35\). Primitive two-cycles exist exactly for \(n\ge4\) other than \(n=7\). The numbers satisfy \(C_n=C_{n-4}+2C_{n-5}+C_{n-6}\) for \(n\ge7\), with initial values \(C_0=C_1=C_2=C_3=0\), \(C_4=2,C_5=5,C_6=3\). If \(\rho\) is the unique positive real root of \(\rho^3-\rho-1=0\), then \(C_n\sim\rho^n/2\). Equivalently, exactly \(2C_n+1\) valuations make \(\Delta\Delta p\leftrightarrow p\) true at all worlds.

## Assumptions and scope

The frame has \(n\ge3\) distinct worlds labelled modulo \(n\), with exactly three successors at each world. The accessibility relation is reflexive and symmetric; transitivity is not assumed. The Boolean valuation of \(p\) is an arbitrary bit vector \(x=(x_i)_{i\in\mathbb Z/n\mathbb Z}\). All uses of \(\Delta\) have the ordinary Kripke truth condition, including reevaluation of inner formulas at every world. The valuation update \(F_n\) sends \(x\) to the truth vector of \(\Delta p\):

\[
(F_n(x))_i=1\quad\Longleftrightarrow\quad x_{i-1}=x_i=x_{i+1}.
\]

A primitive two-cycle is an unordered pair of distinct vectors \(x,y\) satisfying \(F_n(x)=y\) and \(F_n(y)=x\). Fixed valuations are not counted as primitive two-cycles. Labelled worlds are fixed, and cycles are identified only under temporal interchange, not spatial rotation.

## Proof

**1. Fixed points.** If \(F_n(x)=x\) and some coordinate \(x_i=1\), the equality test forces both neighbors of \(i\) to have value one. Propagating around the connected cycle shows that every coordinate equals one. If every coordinate were zero, the next vector would instead be all ones. Hence the sole fixed point is the all-one vector.

**2. Local double-update constraint.** Put \(g(a,b,c)=1\) if \(a=b=c\), and \(g(a,b,c)=0\) otherwise. A valuation is fixed by \(F_n^2\) precisely if, for every cyclic position, its five-bit window obeys

\[
c=g\bigl(g(a,b,c),g(b,c,d),g(c,d,e)\bigr).
\]

Index a \(16\)-state directed transfer matrix \(M\) by four-bit words. For each \((a,b,c,d)\) and bit \(e\), give the transition from \((a,b,c,d)\) to \((b,c,d,e)\) weight one exactly when the displayed constraint holds; all other entries are zero. Closed walks of length \(n\) in this state graph correspond bijectively to cyclic valuations fixed by \(F_n^2\), including for \(n=3\). Therefore, for every \(n\ge3\),

\[
\operatorname{tr}(M^n)=\#\operatorname{Fix}(F_n^2)=2C_n+1.
\]

**3. Exact determinant certificate.** Direct integer calculation of the explicit \(16\)-by-\(16\) matrix, reproducible without external libraries in the accompanying `checker.py` via Newton's identities for matrix traces, yields

\[
\det(\lambda I-M)=\lambda^9(\lambda-1)(\lambda^3-\lambda-1)(\lambda^3+\lambda+1),
\]

and hence

\[
\det(I-zM)=(1-z)(1-z^4-2z^5-z^6).
\]

For a finite matrix the formal power-series identity \(\sum_{n\ge1}\operatorname{tr}(M^n)z^n=-z\,\mathrm d(\log\det(I-zM))/\mathrm dz\) follows by expanding the logarithm. Subtracting the single fixed point at each length and dividing by two gives

\[
\sum_{n\ge3}C_nz^n=-\frac z2\frac{\mathrm d}{\mathrm dz}\log(1-z^4-2z^5-z^6)=\frac{2z^4+5z^5+3z^6}{1-z^4-2z^5-z^6}.
\]

The rational denominator yields the stated recurrence and initial values. Since \(C_3=C_7=0\), \(C_4,C_5,C_6>0\), and \(C_8,\ldots,C_{13}>0\), the recurrence inductively makes every \(C_n\) with \(n\ge8\) positive.

**4. Exponential growth.** The transfer characteristic polynomial shows that the unique eigenvalue of largest modulus is the positive real root \(\rho\) of \(\lambda^3-\lambda-1\), with multiplicity one. For completeness, \(1.32<\rho<1.33\). The nonreal roots of that cubic have modulus \(\rho^{-1/2}<1\). The real root of \(\lambda^3+\lambda+1\) has modulus between \(0.68\) and \(0.69\), and its conjugate roots consequently have modulus less than \(1/\sqrt{0.68}<1.22<\rho\). The other nonzero eigenvalue is one. Consequently \(\operatorname{tr}(M^n)=\rho^n+o(\rho^n)\), and \(C_n\sim\rho^n/2\).

## Verification

The supplied `checker.py` is stand-alone Python 3 code. It builds \(M\) from the five-bit local predicate, derives its exact characteristic polynomial from sixteen integer traces using Newton's identities, and checks the asserted factorization. Separately, it exhaustively evaluates every one of the \(2^n\) valuations for each \(3\le n\le14\), directly compares \(F_n^2(x)\) with \(x\), checks the unique fixed point, and verifies the first twelve ring counts and recurrence. Its expected completion line is `ALL_CHECKS_OK`. Enumeration is a finite cross-check; the proof for all \(n\ge3\) is the transfer-matrix argument above.

## Relationship to prior work

The semantics of the non-contingency operator are standard and are used, for example, by Wang and Zenger in their 2026 study of proof theory for non-contingency logic. On cyclic three-neighbor frames the valuation update coincides with elementary cellular automaton rule 129, and complementation conjugates it to the classical rule 126. Thus the update rule and finite-ring dynamics are not proposed as new. Existing cellular-automaton studies, including numerical Koopman spectra for finite ring sizes and reports about limiting cycle lengths, overlap in finite examples and underlying dynamics. The claim here is specifically the closed formula valid at every ring length, its exact zero/nonzero cutoff, and the asymptotic constant obtained from the transfer determinant. In particular, computed spectra at finitely many ring lengths are not a uniform all-length enumeration theorem.

## Limitations

The result counts primitive *temporal two-cycles* only, not arbitrary periods or basins. It assumes one Boolean atom, the specified reflexive symmetric three-neighbor cycle frames, and labelled spatial positions. This is a self-review, not independent verification. Prior cellular-automaton literature may include an equivalent enumeration in different notation; this priority risk remains open despite the specific searches and comparisons reported separately.

## References

- Yunsong Wang and Lukas Zenger, *Proof Theory for Non-Contingency Logic*, arXiv:2609.38975, first posted 2026-09-30. https://arxiv.org/abs/2609.38975
- Qingying Zhu and Serge Richard, *Elementary cellular automata: spectral properties of Koopman operator for finite periodic realizations*, arXiv:2610.10967, first posted 2026-10-07. https://arxiv.org/abs/2610.10967
- H. P. Stricker, *Classification of Elementary Cellular Automata Based on Their Limit Cycle Lengths in Z/k*, *Complex Systems* 32 (2023), 229–258, doi:10.25088/ComplexSystems.32.3.229.
- Eric W. Weisstein, *Rule 126*, MathWorld, https://mathworld.wolfram.com/Rule126.html.
