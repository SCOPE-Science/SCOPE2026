# Exact 2-adic quotient closures of weighted even-power binary forms

## Finding
Let \(n\ge4\) be even, let \(c\) be any odd integer, and define \(F_{n,c}(x,y)=x^n+c y^n\). Write \(s=\nu_2(n)\), \(h=s+2\), and \(q=2^h\). For \(R_{n,c}=\{F_{n,c}(x,y)/F_{n,c}(z,w):x,y,z,w\in\mathbb Z_{\ge0},\ F_{n,c}(z,w)\ne0\}\), the following is an exact classification of its closure in \(\mathbb Q_2\).

If \(c\equiv-1\pmod q\), then \(\overline{R_{n,c}}=\mathbb Q_2\). Otherwise put \(d=\nu_2(1+c)\), so \(1\le d<h\), and set
\[
(b_0,b_1,b_2)=(1,c,1+c),\qquad (d_0,d_1,d_2)=(0,0,d),\qquad u_i=b_i/2^{d_i}.
\]
Then
\[
\boxed{\overline{R_{n,c}}=\{0\}\;\cup\!\bigcup_{k\in\mathbb Z}\ \bigcup_{0\le i,j\le2}
2^{nk+d_i-d_j}\frac{u_i}{u_j}\left(1+2^{h-\max(d_i,d_j)}\mathbb Z_2\right).}
\]
All nine displayed kinds of balls are genuinely contained in the closure, although some coincide. Consequently the precise set of finite valuations is
\[
\{\nu_2(r):r\in\overline{R_{n,c}}\setminus\{0\}\}
=n\mathbb Z+\{0,d,-d\}.
\]
In particular, the closure is never all of \(\mathbb Q_2\) in this second branch. The exact unit class of each valuation shell is determined by the boxed formula, not only its valuation.

## Assumptions and scope
The variables of the form range over nonnegative integers, which are dense in \(\mathbb Z_2\). The exponent is an even integer at least four, and \(c\) is odd, possibly negative. Quotients with zero denominator are excluded. Closure is in the ordinary \(2\)-adic topology. In the second branch, \(d\) is strictly smaller than \(h\), so every \(b_i\) is nonzero and every displayed unit \(u_i\) is well-defined and odd. No claim is made about odd exponents, even coefficients, or other primes.

## Proof
The elementary unit-power identity, for even \(n\) and \(s=\nu_2(n)\ge1\), is
\[
\{v^n:v\in\mathbb Z_2^\times\}=1+2^{s+2}\mathbb Z_2.
\]
Indeed \(\mathbb Z_2^\times\cong\{\pm1\}\times(1+4\mathbb Z_2)\), and raising the second factor to \(n=2^s t\) with \(t\) odd maps it onto \(1+2^{s+2}\mathbb Z_2\), by the \(2\)-adic logarithm (or an elementary binary-digit lift).

Suppose \(c\not\equiv-1\pmod q\). Denote \(B_0=1+q\mathbb Z_2\), \(B_1=c+q\mathbb Z_2\), \(B_2=1+c+q\mathbb Z_2\). Since \(n\ge h\) whenever \(n\ge4\) is even, examining the smaller of the valuations of \(x,y\) gives the **exact full value-set closure**
\[
\overline{F_{n,c}(\mathbb Z_{\ge0}^2)}
=\{0\}\cup\bigcup_{v\ge0}2^{nv}(B_0\cup B_1\cup B_2).
\]
If one input has strictly smaller valuation than the other, the higher-power term is a multiple of \(2^n\) after normalization, hence of \(q\), giving \(B_0\) or \(B_1\). If the two input valuations agree, normalize both to odd units and obtain \(B_2\). Conversely, every element of each \(B_i\) is obtained with odd inputs and the other input chosen zero when appropriate; surjectivity of the unit-power map proves equality. The zero input pair gives zero.

Every \(B_i=b_i+q\mathbb Z_2\) has valuation exactly \(d_i\), because \(d_i<h\). Therefore
\[
B_i=2^{d_i}u_i(1+2^{h-d_i}\mathbb Z_2).
\]
For any two of these cosets,
\[
B_i/B_j=2^{d_i-d_j}\frac{u_i}{u_j}
(1+2^{h-\max(d_i,d_j)}\mathbb Z_2).
\]
The identity holds because the two unit subgroups are nested and their quotient is the larger one. Taking ratios of the exact value-set closure produces the boxed union, with \(k=v-v'\in\mathbb Z\). Conversely, any element of any displayed ball is such a ratio of two nonzero \(2\)-adic values, hence a limit of rational ratios by continuity of division.

The union is closed after including zero: on any compact annulus avoiding zero there are only finitely many possible integer shifts \(k\) in the valuation equation \(nk+d_i-d_j\), and every individual ball is clopen. Any other accumulation can only be at zero, which is already included. This proves the exact closure. Its possible valuations are precisely \(n\mathbb Z+\{0,d,-d\}\); since \(n\ge4\), at most three residue classes out of \(n\) occur, proving non-density.

If \(c\equiv-1\pmod q\), the unit-power identity gives an odd \(\alpha\in\mathbb Z_2\) with \(\alpha^n=-c\). Thus \(X^n+c\) has a simple root \(\alpha\) in characteristic zero. By the analytic simple-zero quotient-density criterion (or Antony--Barman--Miska's binary-diagonal theorem), ratios of values of \(F_{n,c}\) are dense in \(\mathbb Q_2\). This completes both branches.

## Verification
A standalone standard-library script, `verify.py`, independently enumerates all residue classes of the form modulo \(2^6\), \(2^7\), and \(2^8\) for even exponents \(4,6,8,10,12,14,16,18,20,24,32\), 16 small odd coefficients, and every nonsplit case. It compares the computed residue image with the theorem's three-coset formula; 456 comparisons pass. It also performs 2,176 finite checks of the claimed three valuation-residue shells. Execute `python3 verify.py` to reproduce. These tests check finite congruences only; the infinite statement follows from the unit-power identity and proof above.

## Relationship to prior work
Antony, Barman and Miska (2022, arXiv:2201.04372v1, Theorem 1.1(1)) proved the **density dichotomy** for binary diagonal forms \(a x^n+b y^n\): in this case density is equivalent to \(c\equiv-1\pmod{2^{s+2}}\). They do not provide the complete nonsplit topological closure or its unit cosets. The present statement agrees with their dichotomy and supplies the missing exact descriptions.

Miska, Murru and Sanna (2018, arXiv:1807.08947v2, formula (5)) determine the value-set closure of unweighted sums of powers for exponents \(4,8,16\). The cases \(c\equiv1\pmod q\) are equivalent to unweighted sums because \(c\) is an \(n\)-th power in \(\mathbb Z_2^\times\); these are acknowledged as prior-covered when a complete unweighted classification is available. The density branch \(c\equiv-1\pmod q\) is likewise prior-covered. The substantive additional part is the exact nonsplit closure for the remaining weighted classes \(c\not\equiv\pm1\pmod q\), for every even \(n\), including the precise quotient balls and their unit groups rather than a yes/no density test. The existing unit-power criterion is used explicitly and is not claimed as new.

## Limitations
This theorem is a classification in \(\mathbb Q_2\), not an assertion about real-density or other completions. The proof is elementary once the unit-power map is identified; it does not claim a new Hensel lemma or density criterion. The finite verifier is supplementary, not an infinite certificate. Full coverage by all unpublished, unindexed or implicit earlier local-value classifications has not been established; the most relevant accessible primary full texts were inspected and are named above. Independent mathematical audit has not occurred.

## References
1. Deepa Antony, Rupam Barman, Piotr Miska, *p-Adic quotient sets: diagonal forms*, arXiv:2201.04372v1, posted 2022-01-12, Theorem 1.1 and Lemma 3.1; https://arxiv.org/abs/2201.04372.
2. Piotr Miska, Nadir Murru, Carlo Sanna, *On the p-adic denseness of the quotient set of a polynomial image*, arXiv:1807.08947v2 (initial posting 2018-07-24), Theorem 1.9 and equation (5); https://arxiv.org/abs/1807.08947.
3. Deepa Antony, Rupam Barman, *On p-adic denseness of quotients of values of integral forms*, arXiv:2308.08907v1 (initial posting 2023-08-17); https://arxiv.org/abs/2308.08907.
