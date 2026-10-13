# Three-bit Sahi positivity for all increasing functions under product measures

## Finding

Let \(X=(X_1,X_2,X_3)\) have independent Bernoulli coordinates with arbitrary parameters \(p_1,p_2,p_3\in[0,1]\). For every three coordinatewise nondecreasing, nonnegative, real-valued functions \(f,g,h:\{0,1\}^3\to[0,\infty)\), write \(\mathbb E\) for expectation at these parameters and define the symmetric trilinear functional

\[
E_3(f,g,h)=2\mathbb E[fgh]+\mathbb E[f]\mathbb E[g]\mathbb E[h]
-\mathbb E[f]\mathbb E[gh]-\mathbb E[g]\mathbb E[fh]
-\mathbb E[h]\mathbb E[fg].
\]

**Theorem.** For every such \(p_1,p_2,p_3,f,g,h\), one has \(E_3(f,g,h)\ge 0\). This verifies Sahi's three-function correlation inequality for the entire three-coordinate Bernoulli product cube, including heterogeneous and deterministic coordinates.

## Assumptions and scope

The order on \(\{0,1\}^3\) is coordinatewise. Functions are nonnegative and increasing; no equal-distribution or identical-function hypothesis is imposed. Only a product measure is asserted. The theorem makes no claim for four or more Bernoulli coordinates or for a general dependent FKG measure. It is a universal inequality certified by a complete finite integer identity rather than a sample of parameter choices.

## Proof

First reduce functions to events. Every nonnegative increasing function \(f\) on a finite partially ordered set has a finite nonnegative layer-cake expansion

\[
f=\sum_{r=1}^{m}(a_r-a_{r-1})\mathbf1_{\{f\ge a_r\}},
\quad 0=a_0<a_1<\cdots<a_m,
\]

where the \(a_r\) are its distinct positive values. The level sets \(\{f\ge a_r\}\) are upper sets. Since \(E_3\) is separately linear in its three arguments, it suffices to prove \(E_3(\mathbf1_A,\mathbf1_B,\mathbf1_C)\ge0\) for any three upper sets of the three-bit Boolean lattice.

Encode a lattice point by an integer \(v\in\{0,\ldots,7\}\), with its three binary digits giving coordinates. Encode an upper set \(A\) by the eight-bit mask \(m_A\), whose bit \(v\) is \(1\) precisely when \(v\in A\). A mask is an upper set exactly if

\[
\forall v,w\in\{0,\ldots,7\},\quad
((m_A\gg v)\mathbin{\&}1)=1,\ v\mathbin{\&}w=v
\ \Longrightarrow\ ((m_A\gg w)\mathbin{\&}1)=1.
\]

The program in `verify.py` enumerates all \(256\) masks and establishes that exactly \(20\) satisfy this condition, including the empty and full sets. The functional is symmetric in \(A,B,C\), so it suffices to consider the \(\binom{22}{3}=1540\) unordered triples with repetition.

Fix such \(A,B,C\). For three independent copies \(x,y,z\) of the cube, define the *integer polarization kernel*

\[
\begin{aligned}
G_{A,B,C}(x,y,z)={}&2\mathbf1_A(x)\mathbf1_B(x)\mathbf1_C(x)
+\mathbf1_A(x)\mathbf1_B(y)\mathbf1_C(z)\\
&-\mathbf1_A(x)\mathbf1_B(y)\mathbf1_C(y)
-\mathbf1_B(x)\mathbf1_A(y)\mathbf1_C(y)\\
&-\mathbf1_C(x)\mathbf1_A(y)\mathbf1_B(y).
\end{aligned}
\]

Independence of the copies shows exactly, term by term, that

\[
\mathbb E[G_{A,B,C}(X^{(1)},X^{(2)},X^{(3)})]
=E_3(\mathbf1_A,\mathbf1_B,\mathbf1_C).
\]

For \(\mathbf k=(k_1,k_2,k_3)\in\{0,1,2,3\}^3\), set

\[
c_{\mathbf k}(A,B,C)=
\sum_{\substack{x,y,z\in\{0,1\}^3\\x_i+y_i+z_i=k_i\ (i=1,2,3)}}
G_{A,B,C}(x,y,z).
\]

Grouping the three replicas by their coordinate counts yields the *exact polynomial identity*

\[
E_3(\mathbf1_A,\mathbf1_B,\mathbf1_C)
=\sum_{\mathbf k\in\{0,1,2,3\}^3}
c_{\mathbf k}(A,B,C)
\prod_{i=1}^3p_i^{k_i}(1-p_i)^{3-k_i}.
\]

There are \(64\) integer coefficients for each triple. The supplied self-contained Python 3 program enumerates all \(1540\) unordered upper-set triples and all \(512\) triples of cube points, calculates every \(c_{\mathbf k}\) by the displayed integer sum, and **asserts each is nonnegative**. It exhausts exactly \(1540\cdot64=98560\) coefficients. Its output reports \(33057\) positive coefficients, \(65503\) zero coefficients, largest coefficient \(18\), and smallest positive coefficient \(1\). Each monomial \(\prod_i p_i^{k_i}(1-p_i)^{3-k_i}\) is nonnegative on the full closed unit cube. Therefore every event-triple functional is nonnegative. Trilinearity and the nonnegative layer-cake coefficients give the theorem for all three functions.

The finite enumeration covers all masks and all point triples; it is a complete certificate for this fixed three-dimensional statement, not a finite approximation to the probability parameter continuum.

## Verification

Run `python3 verify.py` with an ordinary Python 3 interpreter from the folder containing this file. The program uses only the Python standard library. It asserts each of the \(98560\) nonnegative coefficient inequalities and independently checks the polarization expansion against direct event probabilities for **every** upper-set triple, with heterogeneous exact rational parameters \((p_1,p_2,p_3)=(1/3,2/5,3/7)\). A separate uniform-parameter normalization check is also performed for every triple. The expected final line is `EXACT_VERIFICATION PASS`; the enumerator reports `UPSETS 20`, `UNORDERED_TRIPLES 1540`, and `BERNSTEIN_CELLS 98560`.

As an illustrative genuinely overlapping event triple, take \(A=\{X_1=1\text{ or }X_2=1\}\), \(B=\{X_2=1\text{ or }X_3=1\}\), and \(C=\{X_1=1\text{ or }X_3=1\}\). At \(p_1=p_2=p_3=1/2\), the exact functional equals \(1/64>0\); its three pairwise intersections are distinct events.

## Relationship to prior work

Sahi's 2008 higher-correlation program and Lieb--Sahi's 2021 work formulate the higher-order inequality and prove restricted classes, including arbitrary monotone functions in two dimensions. Kahn's October 16, 2022 manuscript (primary classification 60C05) explicitly identifies the three-event inequality as a difficult open general question. The present theorem supplies the first higher Boolean dimension \(\{0,1\}^3\) for three arbitrary increasing functions under product laws; it does not claim the unrestricted Sahi conjecture.

Gladkov's 2023 preprint (published 2024) obtains a different multi-event inequality under the **equal pairwise-intersection** condition. The displayed example has distinct pairwise intersections and therefore does not follow from that specialized hypothesis. Kahn's rigidity theorem for certain independent event pairs is likewise logically weaker than the stated universal nonnegative three-event functional. The restriction to two-dimensional monotone functions in Lieb--Sahi is not a three-coordinate result. The exact coefficient method here makes a complete, checkable finite case rather than asserting a general lattice inequality.

## Limitations

No assertion is made for four-bit Boolean cubes, general non-product FKG distributions, arbitrary increasing functions with negative values, or more than three input functions. The argument includes an exhaustive integer computation, so reproducing the supplied code is required to check the finite coefficient positivity component. The method does not give a dimension-free symbolic proof or classify equality cases. A separate independent review of correctness and priority has not been performed; algebraically equivalent earlier proofs under different descriptions remain possible.

## References

1. Jeff Kahn, *A note on positive association*, arXiv:2210.08653v1 (first publicly submitted October 16, 2022), https://arxiv.org/abs/2210.08653 .
2. Elliott H. Lieb and Siddhartha Sahi, *On the extension of the FKG inequality to n functions*, arXiv:2107.09838 (first submitted July 21, 2021), https://arxiv.org/abs/2107.09838 .
3. Siddhartha Sahi, *Higher correlation inequalities*, Combinatorica 28 (2008), 209–227.
4. Nikita Gladkov, *A strong FKG inequality for multiple events*, arXiv:2305.02653 (first submitted May 4, 2023), https://arxiv.org/abs/2305.02653 .
