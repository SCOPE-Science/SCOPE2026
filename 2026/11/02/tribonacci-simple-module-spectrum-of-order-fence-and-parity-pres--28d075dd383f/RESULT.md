# Tribonacci simple-module spectrum of order-, fence-, and parity-preserving partial injections

## Finding
For every integer \(n\ge1\) and every commutative unital ring \(K\), the semigroup algebra of the order-, fence-, and parity-preserving symmetric inverse submonoid \(S_n=IOF_n^{\mathrm{par}}\) admits an explicit finite matrix-product decomposition
\[
K[S_n]\cong K\times\prod_{(p,w):m_{n,p,w}>0}M_{m_{n,p,w}}(K).
\]
Here \(p\in\{\mathrm{odd},\mathrm{even}\}\), \(w\) is a finite word over \(\{1,E,O\}\), \(a_{\mathrm{odd}}=1\), \(a_{\mathrm{even}}=2\), \(c(w)=\#_1(w)+2\#_E(w)+3\#_O(w)\), \(u(w)=\#_E(w)+\#_O(w)\), and
\[
m_{n,p,w}=\begin{cases}
\displaystyle\binom{\lfloor(n-a_p-c(w))/2\rfloor+u(w)+1}{u(w)+1},&a_p+c(w)\le n,\\
0,&a_p+c(w)>n.
\end{cases}
\]
The isolated \(K\) factor is essential: the semigroup algebra is *uncontracted*, so its empty partial map remains a basis element. Distinct nonempty \((p,w)\) give distinct blocks even if their degrees coincide.

Let \(d_{n,r}\) be the number of matrix factors associated with partial maps of rank \(r\), with \(d_{n,0}=1\). The complete rank-refined class-count series is
\[
\sum_{n\ge0}\sum_{r=0}^{n}d_{n,r}t^rz^n
=\frac{1}{1-z}\left(1+\frac{t(z+z^2)}{1-t(z+z^2+z^3)}\right).
\]
At \(t=1\), the number \(D_n=\sum_rd_{n,r}\) of matrix factors, equivalently the number of irreducible modules over any field or the center dimension over a field, obeys
\[
\sum_{n\ge0}D_nz^n=\frac{1+z+z^2}{1-z-z^2-z^3},\qquad
D_0=1,\ D_1=2,\ D_2=4,\ D_n=D_{n-1}+D_{n-2}+D_{n-3}\ \ (n\ge3).
\]
The \(n=0\) convention contains only the empty partial map. The first values for \(n\ge1\) are \(2,4,7,13,24,44,81,149,274,504,927\).

## Assumptions and scope
The ordered ground set is \([n]=\{1,\dots,n\}\). An element is an injective partial map whose domain and image carry their induced ordinary order and induced alternating fence relation \(1\prec2\succ3\prec4\succ\cdots\), and whose values have the same parity as their arguments. Preservation is required both for the transformation and its inverse. Multiplication is composition with the right operand applied first. The coefficients \(K\) may have arbitrary characteristic; no semisimplicity of \(K\) is assumed when it is not a field. The phrase “simple-module spectrum” refers to the matrix factor degrees when \(K\) is a field. The parameter words include the empty word, describing singleton partial maps.

## Proof
**1. Signature criterion.** Write each nonempty subset as \(A=\{a_1<\cdots<a_r\}\) and let \(\sigma(A)=(p,w)\), where \(p\) is the parity of \(a_1\), and each consecutive gap \(a_{i+1}-a_i\) is encoded as \(1\) if it equals one, \(E\) if positive and even, and \(O\) if odd and at least three. The ordinary-order-preserving partial bijection \(A\to B\), when it exists, is unique. It preserves parity and the alternating fence in both directions if and only if \(\sigma(A)=\sigma(B)\): adjacent points in the induced fence correspond precisely to consecutive points with gap one; the parity of all coordinates is reconstructed from the initial parity and successive gap parities. This is the same classification mechanism as the four conditions in Sareeto–Koppitz [1, Proposition 1]. The empty subset is a separate signature.

**2. Multiplicity of a signature.** The smallest first element of parity \(p\) is \(a_p\). A letter \(1\) forces a gap of one; \(E\) allows gap \(2+2k\); \(O\) allows \(3+2k\), with \(k\ge0\). The first vertex can be displaced to \(a_p+2k_0\). Hence a realization is uniquely determined by \(u(w)+1\) nonnegative slack variables whose sum is at most \(\lfloor(n-a_p-c(w))/2\rfloor\). Adjoining a final slack gives an ordinary stars-and-bars count \(\binom{B+u(w)+1}{u(w)+1}\). If the minimal terminal position exceeds \(n\), no such subset exists.

**3. Matrix units.** Every map \(s\in S_n\) restricts to a map between arbitrary subsets of its domain; the resulting set of partial maps is closed under restrictions and inverses. Set
\[
\llbracket s\rrbracket=\sum_{A\subseteq\operatorname{dom}s}(-1)^{|\operatorname{dom}s|-|A|}(s|_A)\quad\in K[S_n].
\]
Boolean Möbius inversion shows that these elements form a \(K\)-basis, with inverse transformation \((s)=\sum_{A\subseteq\operatorname{dom}s}\llbracket s|_A\rrbracket\). Direct inclusion–exclusion, or the established finite-inverse-semigroup groupoid-basis theorem [4], gives
\[
\llbracket s\rrbracket\llbracket t\rrbracket=\begin{cases}
\llbracket st\rrbracket,&\operatorname{dom}s=\operatorname{im}t,\\0,&\text{otherwise}.
\end{cases}
\]
For any fixed signature \(\sigma\), there is exactly one element \(s_{A,B}\) mapping each ordered subset \(A\) to a subset \(B\) with that signature. Therefore \(\llbracket s_{A,B}\rrbracket\) are genuine matrix units indexed by the \(m_{n,p,w}\) subsets of that signature. Distinct signatures multiply to zero. The empty signature yields a single \(1\times1\) factor. This proves the decomposition integrally, and hence over every commutative unital \(K\).

**4. Rank-refined generating series.** A nonempty signature of rank \(r\) consists of an initial vertex of smallest possible value \(1\) or \(2\), followed by \(r-1\) letters of minimal gap weights \(1,2,3\). A signature is realizable on \([n]\) exactly when its minimal terminal position is at most \(n\). Weighting rank by \(t\), ground-set size by \(z\), and adding arbitrary unused terminal space contributes a factor \((1-z)^{-1}\). Summation over all words produces
\[
\frac1{1-z}\left(1+\sum_{r\ge1}t^r(z+z^2)(z+z^2+z^3)^{r-1}\right),
\]
which is the displayed bivariate rational series. Substituting \(t=1\) and simplifying yields the Tribonacci generating function, including its initial conditions and recurrence. Every matrix algebra over a field has one irreducible module of the corresponding degree; the center has one scalar coordinate per block.

## Verification
The standalone file `verify_fence_spectrum.py` implements independent finite enumeration and exact integer checks with only the Python standard library. For every \(1\le n\le11\) it enumerates domain subsets, reconstructs all signature classes, checks every binomial block degree, the number of factors, and the predicted algebra dimension \(\sum m_{n,p,w}^2\). For every \(1\le n\le7\) it also enumerates partial maps directly from parity and gap preservation. For every \(1\le n\le6\), it verifies the displayed Möbius product law for **every ordered pair** of basis maps by actual finite inclusion–exclusion in the original semigroup algebra. It returns `VERIFY_OK: matrix-block census and integral Mobius multiplication`. Finite testing is a check, not the proof for arbitrary \(n\).

## Relationship to prior work
Sareeto and Koppitz [1] introduced the monoid and characterized its partial injections, the starting point for the signature proof. Their subsequent paper [2, Proposition 2] already establishes the Green-equivalence structure and triviality of \(\mathcal H\)-classes: neither the signature/D-class relation nor trivial maximal subgroups is claimed as new here. Their presentation [3] is also prior work. The abstract groupoid/Möbius matrix decomposition for finite inverse semigroups is established by Steinberg [4] and earlier Munn–Solomon theory; it is not claimed as new. The assessed contribution is the **explicit full degree spectrum indexed by parity and gap words, its exact binomial formula, and the rank-refined rational generating function yielding a Tribonacci center/simple-module count**. This is a concrete representation-theoretic and enumerative specialization that requires counting realizations of the known equivalence classes rather than merely quoting their existence.

## Limitations
No new general finite-inverse-semigroup structure theorem is asserted. The center-dimension and irreducible-module interpretations are stated only over fields, while the matrix decomposition itself is valid over commutative unital rings. Related literature may implicitly count the same gap-signature classes under different terminology; the searches and inspections described in the review do not establish exhaustive publication priority. The finite verifier stops at the stated bounds and is not substituted for the proof.

## References
1. A. Sareeto and J. Koppitz, *The rank of the semigroup of order-, fence-, and parity-preserving partial injections on a finite set*, arXiv:2208.03202v1, publicly submitted 2022-08-05. https://arxiv.org/abs/2208.03202
2. A. Sareeto and J. Koppitz, *The maximal subsemigroups of the ideals on a monoid of partial injections*, arXiv:2403.06957v1, publicly submitted 2024-03-11. https://arxiv.org/abs/2403.06957
3. A. Sareeto and J. Koppitz, *A presentation for a submonoid of the symmetric inverse monoid*, arXiv:2310.15809v1, publicly submitted 2023-10-24. https://arxiv.org/abs/2310.15809
4. B. Steinberg, *A Groupoid Approach to Discrete Inverse Semigroup Algebras*, arXiv:0903.3456v1 (2009). https://arxiv.org/abs/0903.3456
