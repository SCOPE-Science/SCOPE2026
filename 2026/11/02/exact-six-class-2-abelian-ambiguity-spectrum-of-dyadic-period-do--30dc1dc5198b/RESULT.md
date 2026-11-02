# Exact six-class 2-Abelian ambiguity spectrum of dyadic period-doubling factors

## Finding
Let \(p=\psi^\omega(0)\) be the binary period-doubling word, where \(\psi(0)=01\) and \(\psi(1)=00\). For an integer \(k\ge3\), let \(N=2^k\) and let \(\mathcal F_N\) be the **set of distinct contiguous factors** of \(p\) of length \(N\). Two words are 2-Abelian equivalent if the number of occurrences of every contiguous word of length one or two agrees.

There are exactly six 2-Abelian equivalence classes in \(\mathcal F_N\), and their **multiset of six cardinalities** is determined as follows. Put
\[
A=\left\lfloor\frac N{12}\right\rfloor,\qquad B=\left\lfloor\frac N6\right\rfloor.
\]
For odd \(k\), the multiset is
\[
\boxed{\{2A+1,\;2A+1,\;2A+2,\;2B,\;2B+1,\;2B+1\}}.
\]
For even \(k\), the multiset is
\[
\boxed{\{2A,\;2A+1,\;2A+1,\;2B+1,\;2B+1,\;2B+2\}}.
\]
Repeated numbers represent **different equivalence classes of equal cardinality**. In particular, \(|\mathcal F_N|=3N/2\); the minimum and maximum class sizes are asymptotic to \(N/6\) and \(N/3\), respectively. The first spectra, for \(N=8,16,32,64\), are \((1,1,2,2,3,3)\), \((2,3,3,5,5,6)\), \((5,5,6,10,11,11)\), and \((10,11,11,21,21,22)\).

## Assumptions and scope
All positions start at zero. A *factor* is a consecutive finite block in the one-sided infinite word \(p\); factors are counted **once per distinct string**, not once per occurrence or starting position. For finite \(u=u_0\cdots u_{m-1}\), let \(\overline{0}=1\), \(\overline{1}=0\), and define two words of length \(2m\):
\[
E(u)=\prod_{i=0}^{m-1}0\overline{u_i},\qquad
O(u)=\prod_{i=0}^{m-1}\overline{u_i}0.
\]
The theorem concerns the indicated substitution, the usual overlapping contiguous occurrences of 1- and 2-letter patterns, and all integers \(k\ge3\). It does not address non-dyadic lengths or higher-Abelian equivalence.

## Proof
**1. Exact dyadic factor recursion.** The fixed-point equation \(p=\psi(p)\) gives \(p_{2i}=0\) and \(p_{2i+1}=\overline{p_i}\). Every length-\(2m\) factor starts at an even or odd position, so, for every \(m\ge1\),
\[
\mathcal F_{2m}=E(\mathcal F_m)\cup O(\mathcal F_m).
\]
Each of \(E\) and \(O\) is injective. The word \(p\) contains no `11`, since every substitution image starts with zero and has no internal `11`. For \(m\ge2\), an equality \(E(u)=O(v)\) would force the resulting word to be all zeros (the first family has all even-indexed positions zero, the second all odd-indexed positions zero). This would force \(u=1^m\), impossible for a factor of \(p\). Therefore these two images are disjoint for \(m\ge2\). As \(\mathcal F_2=\{00,01,10\}\), induction gives \(|\mathcal F_{2^j}|=3\cdot2^{j-1}\) for every \(j\ge1\).

**2. Complete endpoint-and-content census.** Fix \(j\ge1\), let \(m=2^j\), and let \(H_j(z,s,t)\) be the number of distinct words in \(\mathcal F_m\) containing \(z\) zeros, with first symbol \(s\) and last symbol \(t\). Only the two zero counts
\[
z_-(m)=\left\lfloor\frac{2m}{3}\right\rfloor,\qquad z_+(m)=z_-(m)+1
\]
occur. At each such \(z\), the endpoint counts have the form
\[
(H_j(z,s,t))_{s,t\in\{0,1\}}=
\begin{pmatrix}a&b\\b&0\end{pmatrix}.
\]
For the base \(m=2\), the matrices for \(z=1\) and \(z=2\) are, respectively, \(\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)\) and \(\bigl(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\bigr)\). In an image under either \(E\) or \(O\), the number of zeros is \(2m-z\). Because the images are disjoint, the endpoint matrix transforms by
\[
(z,a,b)\longmapsto(2m-z,\;2b,\;a+b).
\]
Indeed, \(E(u)\) starts with zero and ends with \(\overline{u_{m-1}}\), while \(O(u)\) ends with zero and starts with \(\overline{u_0}\). Since \(3\nmid m\), the two possible zero counts swap their low/high order under \(z\mapsto2m-z\). Applying this recurrence inductively yields the following exact table (each displayed \(a,b\) belongs to the indicated low/high count):

| Parity of \(j\) | At \(z_-(m)\) | At \(z_+(m)\) |
|---|---|---|
| odd | \(a=\lfloor m/3\rfloor,\ b=a+1\) | \(b=\lfloor m/6\rfloor,\ a=b+1\) |
| even | \(a=\lfloor m/6\rfloor,\ b=a+1\) | \(b=\lfloor m/3\rfloor,\ a=b+1\) |

For clarity, this induction uses only the transformation \((a,b)\mapsto(2b,a+b)\), the interchange of the two count strata at doubling, and the exact congruences \(2^j\equiv2\pmod6\) for odd \(j\), \(2^j\equiv4\pmod6\) for even \(j\). These congruences turn the indicated floors into exact integer identities. Thus every entry, including the endpoint-symmetry \(H_j(z,0,1)=H_j(z,1,0)\), is proved for arbitrary \(j\).

**3. Exact 2-Abelian fibers at the next scale.** Let \(N=2m\), where \(m=2^j\), and fix one of the two possible zero counts \(z\) for factors of length \(m\). Each image word has exactly \(z\) occurrences of `1` and no `11`. Its entire 2-Abelian signature is therefore determined by \(z\), the first symbol, and the numbers of `01` and `10`. The three possibilities, with their exact counts, are:

* \(E(u)\) with \(u\) ending in zero: first symbol `0`, \(|E(u)|_{01}=z\), \(|E(u)|_{10}=z-1\). There are \(a+b\) such distinct words.
* \(O(u)\) with \(u\) starting in zero: first symbol `1`, \(|O(u)|_{01}=z-1\), \(|O(u)|_{10}=z\). There are \(a+b\) such distinct words.
* \(E(u)\) with \(u\) ending in one, **together with** \(O(v)\) with \(v\) starting in one: first symbol `0`, equal `01` and `10` counts \(z\). Their combined number of distinct words is \(2b\).

The three signatures are different; different values of \(z\) also yield different 1-letter counts. Hence the exact class-size triple belonging to each \(z\) is
\[
\boxed{(a+b,\;a+b,\;2b)}.
\]
For \(m\ge4\) (equivalently \(k\ge3\)) all six classes are nonempty. Substituting the endpoint census of Step 2 with \(j=k-1\), and using \(\lfloor m/6\rfloor=\lfloor N/12\rfloor\) and \(\lfloor m/3\rfloor=\lfloor N/6\rfloor\), gives exactly the two parity cases in the theorem. This also shows that the six entries sum to \(3N/2\). The asymptotics follow directly. \(\square\)

## Verification
Run `python3 checker.py` alongside this document, using Python 3's standard library only. The checker constructs direct finite prefixes by iteration of \(\psi\), enumerates all distinct contiguous length-\(2^k\) factors through \(k=10\), and independently checks their 2-Abelian signatures (both 1-letter and 2-letter counts). It cross-compares those direct factors with the separate complete \(E/O\) factor recursion and tests the signature-class breakdown by zero count. The verified spectra for \(k=3,\ldots,10\) all equal the stated formulas; the finite tests corroborate but do not replace the infinite induction above.

## Relationship to prior work
Karhumäki, Saarela and Zamboni introduced and developed \(k\)-Abelian complexity and studied general class counts. Their 2013 work on variations of the Morse–Hedlund theorem computes the *Abelian* complexity of the period-doubling word (Lemma 6), not the six 2-Abelian class sizes here. Parreau, Rigo, Rowland and Vandomme (arXiv:1405.3532, first posted 2014-05-14) study the 2-Abelian complexity of the same period-doubling word. Their Proposition 34 and Corollary 41 determine the complexity through related block-count functions and its 2-regularity; their Proposition 35 characterizes signature equality. These results count distinct signatures, but do not state the exact cardinalities of the six signature fibers at every dyadic length. The present result refines the class-count invariant to its **full six-term ambiguity spectrum** using direct binary desubstitution. General class-count and factor-count results alone do not determine this multiplicity profile.

## Limitations
The formula concerns **distinct** factors, not positional frequencies of occurrences. It is restricted to dyadic lengths at least eight, ordinary contiguous 2-Abelian equivalence, and one fixed binary substitution. At the smaller dyadic lengths, the number of nonempty classes differs; they are intentionally excluded. The argument establishes a mathematical theorem conditional only on the stated definitions, not an independent publication-priority certificate. No claim is made about the novelty of the known 2-regularity or of the general k-Abelian framework.

## References
1. A. Parreau, M. Rigo, E. Rowland, É. Vandomme, *A new approach to the 2-regularity of the ℓ-Abelian complexity of 2-automatic sequences*, arXiv:1405.3532 (first public version 2014-05-14), especially Section 5 and Propositions 34–35.
2. J. Karhumäki, A. Saarela, L. Q. Zamboni, *Variations of the Morse–Hedlund theorem for k-Abelian equivalence*, arXiv:1302.3783 (2013-02-15), Section 4 and Lemmas 6–7.
3. J. Karhumäki, A. Saarela, L. Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, arXiv:1301.5104 (2013-01-22), foundational definitions and complexity framework.
