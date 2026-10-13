# Arithmetic form and transcendence of the exceptional Engel–Pierce set
## Finding
Let \(C\) be the exceptional set in Ahn's Engel–Pierce transfer: the irrational numbers \(x\in(0,1)\) whose Pierce expansion digits are eventually consecutive. For \(x\in C\), let \(N\) be the least index such that \(p_{n+1}(x)=p_n(x)+1\) for every \(n\ge N\). Put \(k=N-1\), \(m=p_N(x)\),
\[
P=\prod_{i=1}^k p_i(x),\qquad r=\sum_{i=1}^k\frac{(-1)^{i-1}}{p_1(x)\cdots p_i(x)},
\]
with the empty-product and empty-sum conventions \(P=1\) and \(r=0\). If \(D_j\) denotes the derangement number, then
\[
x=r+\frac{(-1)^k}{P}\left((-1)^{m-1}D_{m-1}+(-1)^m(m-1)!e^{-1}\right).
\]
Conversely, every admissible finite Pierce prefix followed by a consecutive tail gives a point of \(C\) and satisfies this formula. Therefore
\[
C\subset \mathbb Q+\mathbb Q^{\times}e^{-1},
\]
and every point of \(C\) is transcendental. Hence every algebraic irrational in \(0,1\) is in the image of Ahn's homeomorphism \(\Theta:\mathbb I\to\mathbb I\setminus C\).

## Assumptions and scope
Pierce expansions are normalized as in Ahn: for irrational \(x\in(0,1)\),
\[
x=\sum_{n\ge1}\frac{(-1)^{n-1}}{p_1(x)\cdots p_n(x)},\qquad 1\le p_1(x)<p_2(x)<\cdots.
\]
The set \(C\) and the map \(\Theta\) are exactly those of arXiv:2610.00946v1. The only external transcendence input is the classical theorem that \(e\) is transcendental. No assertion is made about points outside \(C\), and the displayed parametrization is canonical only when \(N\) is chosen as the least onset index of the consecutive tail.

## Proof
Fix a consecutive tail beginning with \(m\), and write
\[
T_m=\sum_{j=0}^\infty\frac{(-1)^j}{m(m+1)\cdots(m+j)}.
\]
The beta-integral identity
\[
\frac1{m(m+1)\cdots(m+j)}=\frac1{j!}\int_0^1 t^{m-1}(1-t)^j\,dt
\]
gives, by absolute domination of the exponential series on \([0,1]\),
\[
T_m=\int_0^1 t^{m-1}e^{t-1}\,dt.
\]
Thus \(T_1=1-e^{-1}\), while integration by parts yields
\[
T_m=1-(m-1)T_{m-1}\qquad(m\ge2).
\]
The derangement numbers satisfy \(D_0=1\), \(D_1=0\), and \(D_n=(n-1)(D_{n-1}+D_{n-2})\). Induction in the preceding recurrence therefore gives
\[
T_m=(-1)^{m-1}D_{m-1}+(-1)^m(m-1)!e^{-1}.
\]

Now split the Pierce series of \(x\in C\) immediately before its canonical consecutive tail. The finite prefix contributes \(r\), and every tail denominator contains the prefix product \(P\), with overall sign \((-1)^k\). Hence
\[
x=r+\frac{(-1)^k}{P}T_m,
\]
which is the asserted formula. Its coefficient of \(e^{-1}\) is
\[
\frac{(-1)^{k+m}(m-1)!}{P}\in\mathbb Q^{\times},
\]
so \(x\) cannot be algebraic: otherwise \(e^{-1}\) would be a rational affine expression in an algebraic number and hence algebraic, contradicting the transcendence of \(e\). Conversely, an admissible strictly increasing prefix followed by \(m,m+1,m+2,\ldots\) is an eventually consecutive Pierce sequence, so its Pierce value belongs to \(C\). Ahn proves that \(\Theta\) maps \(\mathbb I\) bijectively onto \(\mathbb I\setminus C\); therefore every algebraic irrational in \(0,1\), being outside the transcendental set \(C\), lies in the image.

## Verification
The accompanying `verify.py` checks the exact recurrence and derangement closed form for \(1\le m\le100\), checks twenty consecutive tails numerically against the defining alternating Pierce series with the rigorous first-omitted-term bound, and checks seven finite-prefix gluings. It also confirms that the coefficient of \(e^{-1}\) is nonzero in every tested case. Replay output:

`VERIFY_OK recurrence_cases=100 tail_cases=20 prefix_cases=7 max_error_lt_alternating_bound=1 nonzero_e_coeff=1`

These finite checks corroborate the formulas; the proof above, not the finite computation, establishes the all-parameter statement.

## Relationship to prior work
Ahn defines \(C\) precisely as the set of irrational points with eventually consecutive Pierce digits and proves that it is countable and dense and that \(\Theta\) is a homeomorphism onto \(\mathbb I\setminus C\). The inspected full text does not give an arithmetic description of the values in \(C\) or a transcendence statement for them. Shallit's 1984 paper studies explicit Pierce expansions of a different algebraic quadratic family. Varona's 2017 transcendence theorem concerns Pierce series whose cumulative denominators satisfy a specific nonlinear second-order recurrence; the factorial consecutive-tail denominators used here do not satisfy that hypothesis in general. The present result instead evaluates every eventually consecutive Pierce tail explicitly as a rational affine expression in \(e^{-1}\), thereby describing the entire exceptional set arithmetically.

## Limitations
The inclusion \(C\subset\mathbb Q+\mathbb Q^{\times}e^{-1}\) is not claimed to be equality. Different noncanonical choices of where to cut an already-consecutive tail can give different prefix/tail descriptions of the same point; choosing the least onset index \(N\) removes that redundancy. The argument uses the classical transcendence of \(e\) and does not determine algebraic independence or Diophantine approximation properties of points of \(C\).

## References
1. M. W. Ahn, *Baire-category transfer between Engel and Pierce expansions*, arXiv:2610.00946v1 (2026), primary MSC 11K55.
2. J. O. Shallit, *Some Predictable Pierce Expansions*, Fibonacci Quarterly 22 (1984), 332–335, DOI 10.1080/00150517.1984.12429869.
3. J. L. Varona, *The continued fraction expansion of certain Pierce series*, Journal of Number Theory 180 (2017), 573–578, DOI 10.1016/j.jnt.2017.05.005.
4. C. Hermite, *Sur la fonction exponentielle*, C. R. Acad. Sci. Paris 77 (1873), 18–24, 74–79, 226–233, 285–293.
