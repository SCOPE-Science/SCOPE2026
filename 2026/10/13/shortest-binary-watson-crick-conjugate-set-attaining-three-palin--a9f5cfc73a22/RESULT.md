# Shortest binary Watson-Crick conjugate set attaining three palindromes
## Finding
Let the binary Watson-Crick antimorphic involution be
\[
\theta(0)=1,\qquad \theta(1)=0,\qquad
\theta(x_1x_2\cdots x_n)=\theta(x_n)\cdots\theta(x_2)\theta(x_1).
\]
For a binary word \(w\), let \(C_\theta(w)\) denote its set of distinct \(\theta\)-conjugates.

The shortest positive length for which \(C_\theta(w)\) contains three distinct ordinary palindromes is
\[
7.
\]
Exactly two length-\(7\) words attain three:
\[
\mathtt{0100011}
\quad\text{and}\quad
\mathtt{1011100}.
\]
They are binary complements.

For \(w=\mathtt{0100011}\), the three palindromes are
\[
\mathtt{0001000},\qquad
\mathtt{0010100},\qquad
\mathtt{0011100}.
\]
For its complement \(w=\mathtt{1011100}\), they are
\[
\mathtt{1100011},\qquad
\mathtt{1101011},\qquad
\mathtt{1110111}.
\]

## Assumptions and scope
A word \(u\) is a \(\theta\)-conjugate of \(w\) when there exists a word \(v\) such that
\[
uv=\theta(v)w.
\]
For an antimorphic involution, the standard cut description is
\[
C_\theta(w)=\{\theta(v)u:w=uv\}.
\]
Only distinct elements of this set are counted. An ordinary palindrome is a word equal to its reversal; it need not be a \(\theta\)-palindrome.

The claim is restricted to the binary Watson-Crick involution exchanging \(0\) and \(1\). It does not prove the conjectured general upper bound of three palindromes in \(C_\theta(w)\).

## Proof
For every positive binary length \(n\le7\), enumerate all \(2^n\) words. For each word \(w\), enumerate all \(n+1\) cuts \(w=uv\) and form \(\theta(v)u\). Duplicate \(\theta\)-conjugates are removed, and each remaining word is tested directly for equality with its reversal.

The maximum numbers of distinct ordinary palindromes in \(C_\theta(w)\) for lengths \(1,\ldots,7\) are
\[
2,2,2,2,2,2,3.
\]
Thus no word of length at most \(6\) attains three.

At length \(7\), exactly two words attain three:
\[
\mathtt{0100011},\qquad \mathtt{1011100}.
\]
For the first word, the cuts after positions \(1\), \(4\), and \(5\) produce respectively
\[
\mathtt{0011100},\qquad
\mathtt{0010100},\qquad
\mathtt{0001000},
\]
all palindromes. Exhaustion of all \(128\) binary words of length \(7\) shows that there are no further shortest witnesses.

As an independent check on the cut formula, the verifier also constructs \(C_\theta(w)\) directly from the defining equation \(uv=\theta(v)w\): it enumerates every possible \(v\) of length at most \(|w|\), solves for the length-\(|w|\) prefix \(u\), and retains exactly the solutions satisfying the equation. This direct construction agrees with the cut construction for every binary word of lengths \(1\) through \(7\).

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier exhausts every binary word through length \(7\) twice: once using the cut formula and once using the defining equation for \(\theta\)-conjugacy. It requires the two resulting sets to agree word by word, checks the complete palindrome-count distributions, verifies the two length-\(7\) witnesses, and checks their explicit palindrome sets.

The certificate records the full distributions and the complete \(C_\theta(w)\) sets for both shortest witnesses.

## Relationship to prior work
Mahalingam, Pandoh, and Maity study ordinary palindromes and \(\theta\)-palindromes in \(\theta\)-conjugate sets. For arbitrary words they leave the general maximum number of ordinary palindromes in \(C_\theta(w)\) open. Their later journal version reports a computer check through length \(20\), conjectures the general maximum to be three, and gives a binary Watson-Crick example of length \(12\) whose \(\theta\)-conjugate set contains three ordinary palindromes.

The present result does not address that global conjecture. It determines instead the first finite realization of the conjectured ceiling in the canonical binary Watson-Crick case: length \(7\), with exactly two shortest witnesses.

Targeted searches for the two length-\(7\) words, the phrase “shortest three palindromes,” the \(C_\theta\) notation, and Watson-Crick-conjugate aliases located the primary work but no prior shortest-witness classification.

## Limitations
The result is an exact finite boundary statement for one fixed binary antimorphic involution. It neither proves that three is a universal upper bound nor determines shortest witnesses over larger alphabets or different involutions.

A residual originality risk is an unindexed computation or unpublished note containing the same two length-\(7\) witnesses. The published source reports finite computer checks but does not state this shortest-length classification.

## References
1. K. Mahalingam, P. Pandoh, and A. Maity, “Theta palindromes in theta conjugates,” arXiv:2008.00255v1, first public version 2020-08-01; Theory and Practice of Natural Computing 2020, pp. 145–156.
2. K. Mahalingam, A. Maity, and P. Pandoh, “Counting (Watson-Crick) palindromes in Watson-Crick conjugates,” Information and Computation 285, 104863 (2022), DOI 10.1016/j.ic.2021.104863.
