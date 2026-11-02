# Exact square-root-shift compatibility for every second exponent

## Finding

For a nonsquare positive integer \(m\) and any integer \(b\ge1\), consider the existence of a real \(r\) and a nonsquare positive integer \(n\) such that both
\[
r^2+\sqrt m\in\mathbb Q,\qquad r^b+\sqrt n\in\mathbb Q.
\]
The complete answer is
\[
\boxed{\text{such }r,n\text{ exist}\ \Longleftrightarrow\ b=1\ \text{or}\ 2\mid b\ \text{or}\ 4\mid m.}
\]
In particular, for every fixed odd \(b\ge3\), compatibility is equivalent to \(4\mid m\). In any compatible instance, \(\mathbb Q(\sqrt n)=\mathbb Q(\sqrt m)\): allowing different radical shifts never allows different quadratic fields.

## Assumptions and scope

Write uniquely \(m=dk^2\), where \(d>1\) is positive squarefree and \(k\ge1\) is an integer. The second radicand \(n\) may depend on both \(m\) and \(b\) but must be a nonsquare positive integer; \(r\) may be any real number, including a negative one. Powers have integer exponents. The equivalence \(4\mid m\Longleftrightarrow2\mid k\) follows because \(d\) is squarefree. There is no claim about fixing \(n\) in advance.

## Proof

**Quadratic-field locking.** Suppose a compatible pair exists. Write \(r^2=q-k\sqrt d\) with \(q\in\mathbb Q\). Since \(r^2\ge0\), \(q\ge k\sqrt d>0\) and \(r\ne0\). For any integer \(b\ge1\), the element \((q-k\sqrt d)^b=r^{2b}\) is irrational: its conjugate \((q+k\sqrt d)^b\) is strictly larger, since both bases are nonnegative. But \(r^{2b}\) lies both in \(\mathbb Q(\sqrt d)\) and in \(\mathbb Q(\sqrt n)\), because \(r^b\in\mathbb Q(\sqrt n)\). Distinct quadratic fields intersect only in \(\mathbb Q\). Hence their fields coincide. Therefore \(n=de^2\) for a positive integer \(e\), and \(r^b=P-e\sqrt d\) for some \(P\in\mathbb Q\).

**Odd-exponent obstruction.** Suppose now that \(b\ge3\) is odd and \(k\) is odd. Since
\[
r=\frac{r^b}{(r^2)^{(b-1)/2}},
\]
we have \(r=x+y\sqrt d\) for rational \(x,y\ne0\). Comparing the irrational coefficients of \(r^2=q-k\sqrt d\) gives \(2xy=-k\). Put \(u=\nu_2(x)\), \(v=\nu_2(y)\), and \(\delta=\nu_2(d)\in\{0,1\}\). Since \(k\) is odd, \(u+v=-1\).

The coefficient of \(\sqrt d\) in \(r^b\) is
\[
B=\sum_{\substack{1\le j\le b\\j\ \mathrm{odd}}}T_j,\qquad
T_j=\binom bj x^{b-j}y^j d^{(j-1)/2}.
\]
It must equal the integer \(-e\). We prove instead that \(\nu_2(B)<0\) by identifying its unique minimum-valuation summand.

If \(u\ge0\), then \(v=-u-1\le-1\), and
\[
\nu_2(T_b)=bv+\frac{b-1}{2}\delta\le -\frac{b+1}{2}<0.
\]
For each \(h\ge1\) with \(b-2h\ge1\),
\[
\nu_2(T_{b-2h})-\nu_2(T_b)
=\nu_2\!\binom b{2h}+h\bigl(4u+2-\delta\bigr)>0.
\]
Thus \(T_b\) is the unique term of least valuation.

If \(u\le-1\), then \(v=-u-1\ge0\), and, because \(b\) is odd,
\[
\nu_2(T_1)=(b-1)u+v=(b-2)u-1<0.
\]
For each \(h\ge1\) with \(1+2h\le b\),
\[
\nu_2(T_{1+2h})-\nu_2(T_1)
=\nu_2\!\binom b{1+2h}+h\bigl(2(v-u)+\delta\bigr)>0.
\]
Thus \(T_1\) is the unique term of least valuation. In either case the non-Archimedean valuation rule gives \(\nu_2(B)=\min_j\nu_2(T_j)<0\), contradicting \(B=-e\in\mathbb Z\). Necessarily \(k\) is even, equivalently \(4\mid m\).

**Constructions for every allowed case.** For \(b=1\), take \(r=\tfrac12-k\sqrt d\) and \(n=m\). Then
\[
r+\sqrt n=\tfrac12,\qquad r^2+\sqrt m=m+\tfrac14.
\]
For even \(b=2j\), choose any integer \(q>\sqrt m\), set \(r=\sqrt{q-k\sqrt d}>0\), and expand
\[
r^{2j}=(q-k\sqrt d)^j=U_j-E_j\sqrt d,
\]
where \(U_j\in\mathbb Z\) and
\[
E_j=\sum_{\substack{1\le\ell\le j\\\ell\ \mathrm{odd}}}
\binom j\ell q^{j-\ell}k^\ell d^{(\ell-1)/2}\in\mathbb Z_{>0}.
\]
Taking \(n=dE_j^2\) makes \(r^{2j}+\sqrt n=U_j\in\mathbb Q\), while \(r^2+\sqrt m=q\).

Finally, suppose \(b\ge3\) is odd and \(4\mid m\). Set \(h=k/2\in\mathbb Z_{>0}\) and \(r=1-h\sqrt d\). Then
\[
r^2+\sqrt m=1+h^2d,\qquad r^b=V_b-F_b\sqrt d,
\]
with \(V_b\in\mathbb Z\) and
\[
F_b=\sum_{\substack{1\le\ell\le b\\\ell\ \mathrm{odd}}}
\binom b\ell h^\ell d^{(\ell-1)/2}\in\mathbb Z_{>0}.
\]
Choose \(n=dF_b^2\). Both requested expressions are integers. This proves the equivalence for every \(b\ge1\).

For example, \(m=8\), \(b=3\), \(r=1-\sqrt2\), and \(n=50\) yield \(r^2+\sqrt8=3\) and \(r^3+\sqrt{50}=7\).

## Verification

The standalone standard-Python script `verify.py` checks the binomial coefficients using exact rational arithmetic. Across \(20\) squarefree values \(d\), it tests \(58{,}800\) odd-\(k\) rational inputs against the unique negative-valuation lemma; it also checks \(480\) odd-exponent divisible-by-four constructions, \(900\) even-exponent constructions, \(180\) exponent-one constructions, and the displayed example. All checks passed. The theorem for every \(m,b\) follows from the symbolic proof above, not these finite examples. Run `python3 verify.py` with no third-party packages.

## Relationship to prior work

The 2023 Simon Marais Mathematics Competition, Problem B4(b), and its official solution concern *the same* square-root shift in both expressions. Pisani, *On the Open Problem in the 2023 Simon Marais Mathematics Competition* (arXiv:2610.30658v1, 2026), proves the complete allowed-exponent classification when that shift is held fixed. The present theorem instead permits a second shift \(\sqrt n\) chosen after \(m,b\); it classifies that existence problem by an exact congruence condition on the first radicand and provides witnesses for all cases. The field-locking and sharp odd-exponent integrality obstruction are not consequences of the fixed-shift exponent-pair classification.

## Limitations

The claim is existential in the second radicand and does not enumerate all compatible \(r,n\) for a given \(m,b\), nor address nonintegral radical shifts, powers other than positive integers, or prescribed \(n\). The argument is self-contained once standard facts on quadratic fields and rational \(2\)-adic valuations are admitted. Priority for equivalent statements in older unindexed arithmetic literature cannot be ruled out solely by literature searches.

## References

1. Anthony Pisani, *On the Open Problem in the 2023 Simon Marais Mathematics Competition*, arXiv:2610.30658v1 (submitted 2026-10-22), https://arxiv.org/abs/2610.30658.
2. Simon Marais Mathematics Competition, *2023 Solutions*, Problem B4, pp. 14–16 (2023), https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2023solutions.pdf.
