# An exact all-length cyclic image enumerator for elementary Rule 73

## Finding

Let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be the synchronous elementary cellular automaton with Wolfram rule number \(73\), using periodic boundary conditions and **indexed** ring positions, for every integer \(n\ge1\). Put
\[
 a_n=|F_n(\{0,1\}^n)|,\qquad a_0=1
\]
where the last convention is formal. The ordinary generating function \(A(z)=\sum_{n\ge0}a_nz^n\) is given **exactly** by
\[
\begin{split}
A(z)={}&1-2z^2-5z^5-\mathcal L(f_1)-\tfrac12\mathcal L(f_2)
+\tfrac12\mathcal L(f_3)\\
&-\mathcal L(f_4)-\tfrac12\mathcal L(f_5)+\mathcal L(f_6),
\end{split}
\]
where \(\mathcal L(f)=-zf'(z)/f(z)\) and
\[
\begin{aligned}
f_1(z)&=1-z,\\
f_2(z)&=1-z+z^2,\\
f_3(z)&=1-z^2-z^5,\\
f_4(z)&=1-z^2-z^3-z^5,\\
f_5(z)&=1-z-z^3+z^4-z^5+z^6-z^7,\\
f_6(z)&=1-4z+5z^2-2z^3+z^4-4z^5+9z^6-13z^7\\
&\quad+12z^8-7z^9+z^{10}+4z^{11}-6z^{12}+4z^{13}-2z^{14}.
\end{aligned}
\]
All denominators have constant coefficient one, so this is an unambiguous identity of formal power series over \(\mathbb Q\), not merely a numerical fit. In particular, \(A(z)\) is rational with denominator dividing \(Q(z)=\prod_{j=1}^6 f_j(z)\), a polynomial of degree \(34\). The theorem determines the number of distinct one-step reachable ring configurations for **every** positive ring length, including lengths one and two.

The first values are
\[
(a_1,a_2,\ldots,a_{12})=(2,2,5,12,17,34,79,140,275,544,992,1950).
\]
Additional exact examples are \(a_{16}=25156\), \(a_{20}=324082\), and \(a_{24}=4120610\).

## Assumptions and scope

For each ring \(x=(x_0,\ldots,x_{n-1})\), define
\[
(F_n(x))_i=f(x_{i-1},x_i,x_{i+1}),\qquad
f(u,v,w)=\left\lfloor\frac{73}{2^{4u+2v+w}}\right\rfloor\bmod2,
\]
with all indices reduced modulo \(n\). Different rotations are counted as different configurations when their indexed strings differ. Only **one synchronous update** is considered. All arithmetic in the finite certificate is exact integer arithmetic; no unproved numerical spectral estimate is required.

## Proof

**1. Four-vertex predecessor graph.** Let the overlap states be \(00,01,10,11\), indexed \(0,1,2,3\). For \(b\in\{0,1\}\), define the four-by-four Boolean relation \(M_b\) with an edge from \(uv\) to \(vw\) precisely when \(f(u,v,w)=b\). A ring \(y_0\cdots y_{n-1}\) is in \(F_n\)'s image if and only if a closed predecessor walk bears labels \(y_0,\ldots,y_{n-1}\). Equivalently, the Boolean product \(M_{y_0}\odot\cdots\odot M_{y_{n-1}}\) has at least one diagonal entry. This equivalence also holds when the ring has one or two cells, because the closed-walk condition enforces the repeated boundary variables.

**2. Exact finite deterministic presentation.** Encode each Boolean four-by-four matrix by a 16-bit integer, with bit \(4i+j\) indicating the entry in row \(i\), column \(j\). Starting with the identity relation, close under right Boolean multiplication by \(M_0\) and \(M_1\). The explicit breadth-first construction in `verify_rule73.py` produces exactly \(735\) distinct reachable relations; each of the \(735\) states has two listed successor indices. Let \(h(R)\) be one or zero according as \(R\) has a nonzero diagonal, and let the integer linear operator \(T\) act by
\[
(Tg)(R)=g(R\odot M_0)+g(R\odot M_1).
\]
Then
\[
a_n=(T^n h)(I_4)
\]
for every integer \(n\ge0\). The formula counts **output labels**, not predecessor walks with multiplicity.

**3. Finite certificate proving an infinite recurrence.** Write
\[
Q(z)=\prod_{j=1}^6f_j(z)=\sum_{j=0}^{34}q_jz^j.
\]
Using the exact transition list constructed in step 2, the standalone checker evaluates the following **735-component integer vector identity** and tests every component equal to zero:
\[
\boxed{\sum_{j=0}^{34}q_jT^{40-j}h=0.}
\]
This is a finite identity in the complete 735-dimensional relation-state space, not an extrapolation from the initial values \(a_0,a_1,\ldots\). Applying \(T^{n-40}\) proves
\[
\sum_{j=0}^{34}q_ja_{n-j}=0\qquad(n\ge40).
\]
Consequently \(A(z)\) has denominator dividing \(Q(z)\) and numerator degree at most \(39\).

**4. Identification of the numerator.** The claimed logarithmic-derivative expression also has denominator dividing \(Q(z)\) and numerator degree at most \(39\): every term \(-zf_j'/f_j\) has numerator degree at most \(\deg Q\) after multiplication by \(Q\), and \((1-2z^2-5z^5)Q\) has degree at most \(39\). Thus equality of its coefficients through degree \(39\) with the series from step 2 is sufficient. All forty coefficients are compared exactly in the standalone checker. For reproducibility, here are the coefficients from degree zero through degree thirty-nine, in order:

```text
1, 2, 2, 5, 12, 17, 34, 79, 140, 275,
544, 992, 1950, 3668, 6983, 13345, 25156, 47908, 90520, 171287,
324082, 611791, 1156357, 2182656, 4120610, 7777972, 14676588,
27697442, 52258267, 98600611, 186030139, 350966409, 662142884,
1249170818, 2356636139, 4445888749, 8387284578, 15822822600,
29849970182, 56312354870
```

The formal power-series identity follows at every degree, completing the proof.

## Verification

Execute `python3 verify_rule73.py` in an environment with Python 3 and no third-party dependencies. Its verification is constructive: it builds the two four-state label relations from the number 73; enumerates all 735 Boolean relation states; independently evaluates the 735 integer vector equations; verifies the factorized generating-function coefficients; and separately enumerates the literal forward images of every ring of lengths \(1\) through \(14\). It also verifies the recurrence through degree \(100\), although the infinite proof requires only the single full-vector identity at degree \(40\). A successful replay prints `VERIFY_OK`.

## Relationship to prior work

Jen (1989) gives general finite-window predecessor enumeration and identifies Rule 73 as a rule with telescoping preimage recurrences; those results supply substantial historical machinery, but they do not state the present indexed **same-period ring image-count generating function**. Wolfram (2002, page 699) studies the distinctive wall dynamics and possible complex behavior of Rule 73, rather than the exact cyclic image count. A subsequent public elementary-CA Garden-of-Eden census reports finite-ring orphan counts for the 88 inequivalent rules, but not a proved all-length rational formula. General de Bruijn-graph and automata constructions are classical; the asserted contribution is the **specific exact expression and finite all-length certificate** for Rule 73, not the construction of a Boolean-relation automaton in general.

## Limitations

This result counts distinct outputs, not the number of predecessors of each output, and does not characterize images under multiple time steps or classify attractors. Its proof is a reproducible finite integer computation together with a formal linear-algebra argument, not a handwritten classification of the 735 states. The theorem does not assert a certified explicit root-dominance asymptotic. Historical priority remains subject to checking other unpublished or unindexed work, including older finite-basin atlases.

## References

1. Erica Jen, “Enumeration of Preimages in Cellular Automata,” *Complex Systems* **3** (1989), 421–456. https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf
2. Stephen Wolfram, *A New Kind of Science*, Wolfram Media, first published May 14, 2002, page 699 and related notes on Rule 73. https://wolframscience.com/nks/p699--the-threshold-of-universality-in-cellular-automata/
3. Lucas Kang, “Investigation of Rule 73 as Case Study of Class 4 Long-Distance Cellular Automata,” arXiv:1310.3311 (October 11, 2013). https://arxiv.org/abs/1310.3311
4. “Gardens of Eden,” *Elementary CA Zoo*, finite-ring computational census (accessed October 2026). https://cellular.solves.ca/gardens-of-eden
