# Sharp dyadic local densities for triangular-product square conditions

## Finding

Let \(\mathbb Z_2\) be the 2-adic integer ring, equipped with its normalized additive Haar probability measure. Put \(T(a)=a(a+1)/2\), a continuous integer-valued map on \(\mathbb Z_2\). For two independent Haar-uniform indices \(a,b\) and each ordinary integer \(n\), define the **projected dyadic local square density**

\[\delta_2(n)=\Pr\bigl(T(a)T(b)+n\in(\mathbb Z_2)^2\bigr).\]

Then \(\delta_2(0)=5/36\). If \(n\ne0\), write \(h=v_2(n)\ge0\) and \(u=n/2^h\), an odd integer. The complete formula is

\[\boxed{\delta_2(n)=\begin{cases}\frac5{36}\left(1-2^{-(h+1)}\right),&h\text{ odd},\\[2pt]\frac5{36}+2^{-h}c(u),&h\text{ even},\end{cases}}\]

where

\[c(u)=\begin{cases}\frac7{36},&u\equiv1\pmod8,\\[2pt]\frac1{144},&u\equiv3,7\pmod8,\\[2pt]\frac5{72},&u\equiv5\pmod8.\end{cases}\]

In particular,

\[\boxed{\frac5{48}\le\delta_2(n)\le\frac13\quad(n\in\mathbb Z).}\]

The lower bound holds with equality **exactly** when \(v_2(n)=1\), equivalently \(n\equiv2\pmod4\); the upper bound holds with equality **exactly** when \(n\equiv1\pmod8\). Some exact values are \(\delta_2(1)=1/3\), \(\delta_2(2)=5/48\), \(\delta_2(3)=7/48\), \(\delta_2(5)=5/24\), and \(\delta_2(0)=5/36\).

## Assumptions and scope

The variable \(n\) is any fixed ordinary integer, possibly zero or negative. All probabilities refer to **2-adic Haar measure** of the pair of indices, not counting density of actual integer Diophantine solutions. A 2-adic square includes zero; the zero sets relevant to the proof have Haar measure zero. For \(n\ne0\), \(v_2(n)\) denotes the largest \(h\ge0\) for which \(2^h\mid n\), and \(u\) is viewed modulo \(8\) in the displayed formula. The primary arithmetic subject is Diophantine equations and their local solubility densities (MSC2020 11D09).

## Proof

**1. Uniformity of triangular values.** For every \(k\ge1\), define \(T(a)\bmod2^k\) using \(a\bmod2^{k+1}\); this is well defined since

\[T(a+2^{k+1})-T(a)=2^k(2a+2^{k+1}+1).\]

The increment on the right is exactly \(2^k\) modulo \(2^{k+1}\). At \(k=1\), the four values obtained from \(a=0,1,2,3\) contain both residue classes exactly twice. If each residue modulo \(2^k\) has two preimages among the \(2^{k+1}\) indices, lifting each index by adding either \(0\) or \(2^{k+1}\) gives exactly two preimages of each of its two lifts modulo \(2^{k+1}\). Induction proves that \(T(a)\bmod2^k\) is uniform for every \(k\), hence \(T\) pushes Haar measure forward to Haar measure. Two independent indices give independent Haar-uniform \(U=T(a)\) and \(V=T(b)\).

**2. Distribution of the product.** A Haar-uniform \(U\in\mathbb Z_2\) satisfies \(\Pr(v_2(U)=j)=2^{-(j+1)}\), for each \(j\ge0\), and its normalized odd unit is Haar-uniform in \(\mathbb Z_2^\times\). Independence gives, for \(W=UV\),

\[a_k:=\Pr(v_2(W)=k)=\frac{k+1}{2^{k+2}}\qquad(k\ge0).\]

Conditionally on \(v_2(W)=k\), write \(W=2^k\xi\) with \(\xi\) Haar-uniform among odd 2-adic units. A nonzero \(2^e w\) is a square in \(\mathbb Z_2\) precisely if \(e\) is even and \(w\equiv1\pmod8\). An independent uniform unit meets the final congruence with probability \(1/4\).

**3. The parameter zero.** The preceding criterion and the product valuation distribution yield

\[\delta_2(0)=\frac14\sum_{j\ge0}\frac{2j+1}{2^{2j+2}}=\frac5{36}.\]

**4. Positive and negative nonzero parameters.** Fix \(n=2^h u\ne0\), with odd \(u\). Separate the product valuations \(k=v_2(W)\) into three regimes. If \(k<h\), the perturbation \(2^{h-k}u\) is even, so the sum can be a square only for even \(k\), and then with conditional probability \(1/4\). The total contribution is

\[S_h=\frac14\sum_{\substack{0\le k<h\\k\text{ even}}}\frac{k+1}{2^{k+2}}.\]

If \(k=h\), the conditional random odd unit \(\xi\) satisfies \(\xi+u=2Z\), where \(Z\) is Haar-uniform in \(\mathbb Z_2\). Since

\[\Pr(Z\text{ square})=\frac16,\qquad\Pr(2Z\text{ square})=\frac1{12},\]

this regime contributes \(a_h/6\) when \(h\) is odd and \(a_h/12\) when \(h\) is even.

If \(k>h\), then \(W+n=2^h(u+2^{k-h}\xi)\) has valuation exactly \(h\). It cannot be a square when \(h\) is odd. When \(h\) is even, the conditional probabilities in the successive regimes \(k=h+1\), \(k=h+2\), and \(k\ge h+3\) are respectively

\[\frac12\,\mathbf 1_{u\equiv3,7\ (\mathrm{mod}\ 8)},\quad\mathbf1_{u\equiv5\ (\mathrm{mod}\ 8)},\quad\mathbf1_{u\equiv1\ (\mathrm{mod}\ 8)}.\]

The third regime has exact mass

\[\sum_{k\ge h+3}a_k=\frac{h+5}{2^{h+4}}.\]

Hence, for odd \(h\),

\[\delta_2(n)=S_h+\frac{a_h}{6}=\frac5{36}\left(1-2^{-(h+1)}\right).\]

For even \(h\),

\[\delta_2(n)=S_h+\frac{a_h}{12}+\begin{cases}\sum_{k\ge h+3}a_k,&u\equiv1\pmod8,\\[1pt] a_{h+1}/2,&u\equiv3,7\pmod8,\\[1pt]a_{h+2},&u\equiv5\pmod8.\end{cases}\]

Summing these elementary finite/geometric series gives exactly \(\delta_2(n)=5/36+2^{-h}c(u)\), with the three constants stated above.

**5. Optimal uniform bounds.** For odd \(h\ge1\), the formula increases monotonically toward \(5/36\) and is smallest at \(h=1\), giving \(5/48\). For even \(h\ge0\), all three \(c(u)\) values are strictly positive; their maximum is \(7/36\), attained with \(h=0\) and \(u\equiv1\pmod8\), giving \(1/3\). The value at \(n=0\) is between these extremes. The strictness of the inequalities elsewhere proves both equality classifications. \(\square\)

## Verification

Run the self-contained Python 3 program `verify.py` (standard library only) from the same directory. It performs exact-integer triangular-fiber enumerations at levels \(1\le k\le12\), rational disintegration comparisons for \(0\le h\le25\) and four unit classes with both signs, modular-square comparisons through modulus \(512\), direct triangular-value versus independent uniform-product counts through modulus \(128\), and sharp-bound tests for every integer from \(-2000\) to \(2000\). The program prints `VERIFY_OK` on success. These finite checks corroborate the calculations but do not replace the general argument above.

## Relationship to prior work

Bagchi and Zhou-Zheng's 2026 study of triangular-number Diophantine tuples proves a modulo-nine obstruction to integer pairs and states local solvability for primes other than three. This finding instead quantifies the full **index-Haar local square density at the dyadic prime** for every integer parameter, distinguishing exact valuation and odd-unit classes. The earlier algebraic and Pell-equation investigations of triangular-number \(D(n)\)-pairs address existence and construction, not this measure. Bürgisser, Kulkarni, and Lerario's open-access study of random nonarchimedean quadratic equations supplies background on square-unit probabilities and valuation distributions but studies different random coefficient models. Those ingredients do not, by the inspected stated results alone, give the explicit parameter-dependent dyadic density or its sharp extremal classes.

## Limitations

The formula measures pairs of independent 2-adic indices. It neither asserts the existence of positive integer solutions of \(T(a)T(b)+n=z^2\), nor supplies a local-to-global or integer-counting theorem. The motivating preprint's full text was not available in the reviewed sources; its accessible abstract was examined, so unrecognized prior coverage in its body is an acknowledged literature risk. Equivalence to an existing general \(p\)-adic integration formula also remains a possible originality risk. No independent external validation is asserted.

## References

1. S. Bagchi and C. Zhou-Zheng, *Diophantine m-tuples of Triangular Numbers*, arXiv:2608.27697v1 (first public preprint 2026-08-27). https://arxiv.org/abs/2608.27697
2. M. Bliznac Trebješanin, *D(-1)-triples of triangular numbers*, arXiv:2603.29565v1 (2026-03-31). https://arxiv.org/abs/2603.29565
3. P. Bürgisser, A. Kulkarni, and A. Lerario, *Nonarchimedean integral geometry*, Selecta Mathematica 32, article 10 (2026), Section 7.4, DOI:10.1007/s00029-025-01120-y. https://doi.org/10.1007/s00029-025-01120-y
