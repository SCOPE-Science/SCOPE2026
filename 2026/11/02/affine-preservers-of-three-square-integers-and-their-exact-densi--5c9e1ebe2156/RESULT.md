# Affine preservers of three-square integers and their exact density

## Finding
Let \(\mathcal S=\{x^2+y^2+z^2:x,y,z\in\mathbb Z\}\subseteq\mathbb Z_{\ge0}\), including zero. For integers \(a\ge1\), \(b\ge0\), write \(F_{a,b}(n)=an+b\). Then \(F_{a,b}(\mathcal S)\subseteq\mathcal S\) precisely as follows.

If \(b=0\), there is an integer \(j\ge0\) such that \(a=4^j u\) with \(u\equiv1\pmod8\).

If \(b>0\), repeatedly replace \((a,b)\) by \((a/4,b/4)\) while both entries are divisible by four. Write the resulting pair as \((A,B)\). Exactly one of the following conditions must hold:

1. \(4\mid A\) and \(B\equiv1\text{ or }2\pmod4\);
2. \(8\mid A\) and \(B\equiv3\pmod8\).

Equivalently, if \(r=\nu_2(b)\) and \(u=b/2^r\), then the positive-intercept criterion is: \(r\) odd and \(\nu_2(a)\ge r+1\); or \(r\) even, \(u\equiv1\pmod4\), and \(\nu_2(a)\ge r+2\); or \(r\) even, \(u\equiv3\pmod8\), and \(\nu_2(a)\ge r+3\). No map is admissible when \(r\) is even and \(u\equiv7\pmod8\).

Define \(N(X)=\#\{(a,b):1\le a,b\le X,\ F_{a,b}(\mathcal S)\subseteq\mathcal S\}\) for integers \(X\ge1\). Then
\[
N(X)=\left\lfloor\frac X4\right\rfloor B_{12}(X)+\left\lfloor\frac X8\right\rfloor B_3(X)+N(\lfloor X/4\rfloor),\qquad N(0)=0,
\]
where \(B_{12}(X)=\#\{1\le b\le X:b\equiv1,2\pmod4\}\) and \(B_3(X)=\#\{1\le b\le X:b\equiv3\pmod8\}\). Consequently
\[
N(X)=\frac3{20}X^2+O(X).
\]

## Assumptions and scope
The slopes are positive integers, intercepts nonnegative integers, and the three squared variables may be zero or negative. The density assertion counts *positive* intercepts and slopes in an integer square box. The ambient three-square set is nonnegative, and no negative-slope or negative-intercept maps are classified here. The input \(n=0\) is included.

We use Legendre's three-square theorem: a nonnegative integer is in \(\mathcal S\) if and only if it is not \(4^j(8h+7)\) for integers \(j,h\ge0\).

## Proof
**Step 1 (a local reformulation).** In the ring \(\mathbb Z_2\) of 2-adic integers define the open forbidden set
\[
\mathcal E=\bigcup_{j\ge0}\bigl(7\cdot4^j+8\cdot4^j\mathbb Z_2\bigr).
\]
The cylinders are disjoint, their Haar measures sum to \(\mu(\mathcal E)=\sum_{j\ge0}1/(8\cdot4^j)=1/6\), and their only accumulation point outside \(\mathcal E\) is zero. Thus \(\overline{\mathcal E}=\mathcal E\cup\{0\}\); away from zero, membership in \(\mathcal E\) is locally constant. Every 2-adic neighborhood of zero contains subsets of positive measure both inside and outside \(\mathcal E\).

For \(T(n)=an+b\), the required three-square preservation is equivalent to
\[
T^{-1}(\mathcal E)\subseteq\mathcal E\quad\text{inside }\mathbb Z_2.
\]
Indeed the implication from right to left is immediate for nonnegative integers by Legendre. Conversely, if some \(t\in T^{-1}(\mathcal E)\setminus\mathcal E\) is nonzero, a sufficiently small 2-adic neighborhood of \(t\) lies in the complement of \(\mathcal E\) and in \(T^{-1}(\mathcal E)\); it contains a nonnegative integer, a contradiction. If \(t=0\), then \(b\in\mathcal E\), contradicting preservation of the input zero.

**Step 2 (odd slope).** Suppose \(a\) is odd. Then \(T\) is a Haar-measure-preserving homeomorphism. Containment of \(T^{-1}(\mathcal E)\) in \(\mathcal E\), together with equality of their measures \(1/6\), forces equality up to a null set. If \(b\ne0\), the point \(t=-a^{-1}b\in\mathbb Z_2\) is nonzero. A small neighborhood \(U\) of \(t\) is wholly in \(\mathcal E\) or wholly outside it. But \(T(U)\) is a neighborhood of zero, so \(U\cap T^{-1}(\mathcal E)\) and \(U\setminus T^{-1}(\mathcal E)\) both have positive measure. This contradicts equality almost everywhere if \(U\subseteq\mathcal E\), and contradicts containment if \(U\cap\mathcal E=arnothing\). Hence \(b=0\). Multiplication by an odd \(a\) preserves the excluded valuation/residue classes exactly when \(a\equiv1\pmod8\). If \(a\not\equiv1\pmod8\), an odd nonexcluded residue maps to \(7\pmod8\).

**Step 3 (slope exactly twice an odd number).** Let \(a=2u\) with \(u\) odd. If \(b\) is odd, \(T\) sends Haar measure uniformly onto the odd coset, for which the proportion of excluded points is \((1/8)/(1/2)=1/4\). Hence \(\mu(T^{-1}\mathcal E)=1/4>\mu(\mathcal E)=1/6\), contradicting inclusion.

If \(b=2c\), set \(t=-c/u\in\mathbb Z_2\). For every \(j\ge1\), the nonempty preimage \(T^{-1}(7\cdot4^j+8\cdot4^j\mathbb Z_2)\) is a 2-adic cylinder approaching \(t\) as \(j\to\infty\). Inclusion implies \(t\in\overline{\mathcal E}\); hence \(t\pmod8\) is one of \(0,4,7\). But at \(j=1\) the preimage consists of
\[
n\equiv u^{-1}(14-c)\equiv t+14u^{-1}\pmod8.
\]
Because \(14u^{-1}\equiv2\) or \(6\pmod8\), this residue belongs to \(\{1,2,5,6\}\), none of which occurs in \(\mathcal E\pmod8\). This contradiction excludes all such slopes.

**Step 4 (slopes divisible by four).** If \(4\mid a\) and \(4\mid b\), Legendre's criterion implies that \(an+b\) is representable if and only if \((a/4)n+(b/4)\) is representable. Repeatedly divide the common factor four. If the reduced intercept is zero, Step 2 applies, including the slope of valuation zero; Step 3 excludes slopes of valuation one. Otherwise, if the resulting positive intercept \(B\) is not divisible by four, then \(B\equiv1\) or \(2\pmod4\) guarantees that \(An+B\) is never excluded whenever \(4\mid A\). For \(B\equiv3\pmod4\), if \(8\mid A\), all outputs have the fixed residue \(B\pmod8\), and preservation holds exactly when \(B\equiv3\pmod8\). If \(A\equiv4\pmod8\), evaluating at \(n=0\) or \(n=1\), both in \(\mathcal S\), forces a forbidden output \(7\pmod8\). These are all cases. Undoing the common divisions yields the stated valuation formulation.

**Step 5 (count).** The cases at positive intercept split disjointly into \(4\mid a,\ b\equiv1,2\pmod4\), or \(8\mid a,\ b\equiv3\pmod8\), or \(4\mid a,4\mid b\) followed by an admissible reduced pair. This gives the exact recurrence. The two initial terms contribute \(X^2/8+X^2/64+O(X)=9X^2/64+O(X)\); iteration yields \(N(X)=(9/64)X^2\sum_{j\ge0}16^{-j}+O(X)=3X^2/20+O(X)\).

## Verification
The standalone standard-library-only checker `artifacts/verify.py` reconstructs all sums of three squares through 1200 directly and checks Legendre's excluded-class formula. It compares the theorem's classification with direct preservation tests for all \(16512\) pairs \(1\le a\le128\), \(0\le b\le128\) on all representable inputs \(0\le n<1600\). It independently evaluates the counting recurrence by direct enumeration for box sizes through 256. Run `python3 artifacts/verify.py`; the expected final line begins `VERIFY_OK`. These finite tests are corroborative, not substitutes for the 2-adic proof.

## Relationship to prior work
She, Sun, and Zhou (arXiv:2606.04744v1, 2026-06-03) study ternary representations by almost-prime squares and explicitly use the exceptional integers \(4^j(8h+7)\) in Theorem 1.3. Their representation and weighted-sieve results do not classify affine maps preserving the full three-square set. Matijasevick (arXiv:2610.36284v1, 2026-10-26) classifies affine maps of polygonal number sets and sums of two triangular numbers (Theorem 6.7) and gives local-obstruction discussion for sums of two squares (Proposition 7.10); neither addresses sums of three squares. These are distinct value sets, and no implication to the present full classification or pair density was found in the inspected results. Legendre's theorem supplies the classical local characterization on which the proof builds.

## Limitations
An earlier equivalent classification under the language of affine preservers of ternary quadratic-form values cannot be ruled out by the available search. Originality has not been independently certified. This result concerns the unweighted ternary sum of three squares over nonnegative integers, not arbitrary positive ternary quadratic forms or affine maps with negative slope or intercept. The positive-intercept density does not include the exceptional zero-intercept family. The 2-adic measure argument establishes the theorem mathematically; exact finite experiments alone cannot certify the infinite statements.

## References
1. Y.-F. She, Y.-C. Sun, and G.-L. Zhou, *Representations of positive integers by three almost-prime squares*, arXiv:2606.04744v1 (first posted 2026-06-03), https://arxiv.org/abs/2606.04744. Theorem 1.3.
2. M. Matijasevick, *Retriangular numbers and affine maps between polygonal numbers*, arXiv:2610.36284v1 (first posted 2026-10-26), https://arxiv.org/abs/2610.36284. Theorem 6.7 and Proposition 7.10 (different number sets).
3. A.-M. Legendre, classical three-square theorem, cited in the form \(n\notin\{4^j(8h+7):j,h\ge0\}\); see standard histories of sums of three squares.
