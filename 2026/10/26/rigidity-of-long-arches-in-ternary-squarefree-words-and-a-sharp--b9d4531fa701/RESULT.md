# Rigidity of long arches in ternary squarefree words and a sharp five-universality threshold

## Finding
Let \(\Sigma=\{0,1,2\}\). For every finite squarefree word \(w\in\Sigma^*\), let \(\iota(w)\) denote the largest \(k\) for which every word in \(\Sigma^k\) occurs in \(w\) as a scattered subsequence. In the greedy arch factorization of \(w\), every complete arch has length three or four, and **four consecutive length-four arches are impossible**. More precisely, three consecutive length-four arches, if present, have the unique form \(abac\,babc\,abac\) for distinct letters \(a,b,c\), whereas the fourth would be forced to complete the square \((abac\,babc)^2\). The triple is attainable.

Consequently, writing \(m=\iota(w)\) and \(n=|w|\),
\[
 n\le 4m-\lfloor m/4\rfloor+3.
\]
In particular every ternary squarefree word of length \(n\ge4\) obeys
\[
 \iota(w)\ge\left\lfloor\frac{4(n-4)}{15}\right\rfloor+1,
\]
and hence \(\liminf_{n\to\infty}\min_{|w|=n,\,w\text{ squarefree}}\iota(w)/n\ge4/15\). The first improvement beyond the elementary four-position pigeonhole bound is sharp: **every** ternary squarefree word of length \(19\) is \(5\)-subsequence universal, whereas the squarefree length-\(18\) word `010201210120102101` has universality index exactly \(4\).

## Assumptions and scope
A *square* is a factor \(xx\) with \(x\) nonempty; *squarefree* means no such factor occurs. Factors are contiguous, whereas subsequences need not be. We fix the full three-letter alphabet even for a short word missing some letters. Starting at the first position of \(w\), a greedy *complete arch* is the shortest nonempty prefix containing all three symbols; remove it and repeat. The terminal *remainder* misses at least one of the three symbols. The number of complete arches is the standard subsequence-universality index \(\iota(w)\) (Hébrard's arch criterion, as recalled by Adamson, 2023, Section 2). Statements hold for every finite ternary squarefree word, including nonextendible words, with no periodicity or morphicity assumption. For \(n\le3\) the formula for the explicit numerical lower bound is not asserted.

## Proof
**1. Arch lengths.** Every squarefree word on two symbols has length at most three. Indeed, two equal consecutive symbols form a square of length two, so a binary word of length four without an adjacent equality would have to alternate and hence contain a square of length four. Thus every factor of length four of a ternary squarefree word contains all three symbols. A complete greedy arch has length at least three and at most four; a remainder that omits a symbol has length at most three.

**2. Long-arch transition rigidity.** A length-four complete arch starts with three letters but uses only two distinct letters there. Adjacent equal letters would form a square, so those first three letters are \(aba\) with \(a\ne b\), followed by the missing letter \(c\). Hence the arch is \(abac\) with \(a,b,c\) pairwise distinct. Suppose the next complete arch also has length four, say \(xyxz\) with \(x,y,z\) pairwise distinct. The first symbol \(x\) cannot be \(c\) because the boundary would contain \(cc\). If \(x=a\), the choice \(y=b\) repeats the entire block \(abac\), while \(y=c\) creates the square \(acac\) straddling the boundary. If \(x=b\), the choice \(y=c\) creates the square \(cbcb\) across the boundary (the preceding \(c\) followed by \(bcb\)). Thus necessarily \(x=b,y=a,z=c\), yielding the next arch \(babc\). This conclusion is independent of earlier context.

Applying the same transition to \(babc\) forces the third length-four arch to be \(abac\), and a fourth to be \(babc\). The concatenation of four such arches would be \((abac\,babc)^2\), a forbidden square. The sharp three-arch example `0102 1012 0102` is squarefree, as follows directly by checking its factors (also checked by the standalone verifier).

**3. Length and universality.** Among each disjoint group of four consecutive greedy arches at least one has length three. Therefore at least \(\lfloor m/4\rfloor\) of the \(m\) arches have length three, so their aggregate length is at most \(4m-\lfloor m/4\rfloor\). Adding the remainder of length at most three gives the claimed bound. Since \(4m-\lfloor m/4\rfloor=\lceil15m/4\rceil\), \(n\le\lceil15m/4\rceil+3\) implies \(15m/4>n-4\), and the displayed integer lower bound follows for \(n\ge4\). Dividing by \(n\) establishes the asymptotic lower bound; no equality or optimal asymptotic constant is claimed.

**4. Sharp length threshold.** If a ternary squarefree word had four or fewer complete arches, its length would be at most \(4\cdot4-\lfloor4/4\rfloor+3=18\). Hence all length-\(19\) words have index at least five. The length-\(18\) witness `010201210120102101` is squarefree and has greedy factorization `0102 | 012 | 1012 | 0102 | 101`, consisting of four complete arches and a proper remainder. Thus the forcing threshold for five-universality is exactly nineteen, among squarefree ternary words.

## Verification
Run `python3 verify.py` using Python 3 and no third-party packages. The verifier independently enumerates all squarefree words up to length nineteen by checking every appended suffix for squares, confirms that the normalized initial long arch has exactly one admissible long successor and one admissible length-twelve triple, and checks no four consecutive length-four arches occur. It enumerates all \(1830\) squarefree words of length nineteen and directly checks all \(3^5=243\) five-letter subsequences for each. It also checks the length-eighteen witness directly against all target subsequences of lengths one through five. The infinite proof is the elementary local argument above and does not rely on numerical extrapolation.

## Relationship to prior work
Adamson, *Ranking and Unranking k-subsequence universal words* (arXiv:2304.04583v1, 2023), supplies the standard arch-index characterization and unrestricted enumeration. Schnoebelen and Veron, *On arch factorization and subword universality for words and compressed words* (arXiv:2304.11932v1, 2023), studies arch jumping, circular universality, and compression. Grytczuk, Kordulewski, and Pawlik, *Squarefree Extensions of Words* (Journal of Integer Sequences 24, 2021, Article 21.8.7), treats squarefree extension behavior and records the elementary impossibility of binary squarefree words of length four. These background results do not state the three-long-arch rigidity, the improved density bound, or the sharp length-nineteen threshold for the intersection of squarefreeness and subsequence universality. The general arch criterion and binary squarefree bound are prior ingredients, not claimed as new.

## Limitations
The \(4/15\) asymptotic constant is a universal *lower bound*, not proved sharp. The proof does not enumerate the complete distribution of indices among squarefree words, classify all extremizers at length eighteen, or address alphabets of other cardinalities. Literature searches cannot exclude every possible equivalent formulation; no independent mathematical audit has been performed.

## References
1. D. Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583v1, first submitted 2023-04-10, https://arxiv.org/html/2304.04583v1.
2. Ph. Schnoebelen and J. Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:2304.11932v1, first submitted 2023-04-24, https://arxiv.org/html/2304.11932v1.
3. J. Grytczuk, H. Kordulewski, and B. Pawlik, *Squarefree Extensions of Words*, Journal of Integer Sequences 24 (2021), Article 21.8.7, https://cs.uwaterloo.ca/journals/JIS/VOL24/Grytczuk/grytczuk7.pdf.
