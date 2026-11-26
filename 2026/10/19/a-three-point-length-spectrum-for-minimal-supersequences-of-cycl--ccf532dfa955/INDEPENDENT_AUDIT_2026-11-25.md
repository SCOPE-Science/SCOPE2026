# Independent mathematical audit

## correctness

PASS

In a deletion-minimal word any chosen pair of embeddings covers all positions, or an uncovered position could be deleted. Each symbol therefore occurs once or twice. Put C=1...n-1. A single zero forces C on each side with no extra positions, hence C0C, whose two required embeddings are unique. For two zeros, A can always reuse the first instead of a later zero, and B can always reuse the last instead of an earlier zero. If a nonzero symbol j occurs just once, both embeddings must pass through it. The prefix required by A through the cut contains the prefix required by B, so one A-prefix embedding can serve both: minimality forces the left part to equal 0...j-1. The symmetric right requirement is the longer B suffix j+1...n-1,0. Thus the only such word is 0C0, with each position essential. All other candidates have every symbol twice and hence length 2n. The exhibited E_n has a unique embedding of A: its earlier zero and all second copies of nonzero letters are forced in forward order. B must use its later zero and all first copies in reverse forcing order. These embeddings are disjoint and exhaustive for n>=3, proving minimality and attainability, not a classification of every full-length word. For n=2, a word containing both 01 and 10 has at least three runs and therefore contains 010 or 101; minimality gives precisely those two. Inspected RESULT.md lines 23–43, verify.py, VERIFICATION.md and verification_output.txt. The bundled Python 3 alignment enumeration and separate small direct search are finite corroboration, not required for the proof; their recorded outputs were read and not re-executed.

## originality

PASS

The supported distinct contribution is the uniform n>=3 length spectrum for the one-step shift of a distinct-letter permutation, with rigidity of both shorter words and an all-n full-length witness. Earlier opposite binary blocks share precisely the separate n=2 boundary when their blocks are singletons. A distinct cyclic-sequence catalogue entry covers full-length counts at n=3,4,5, but neither shorter layer nor the all-n assertion. General position characterizations, fixed-input enumeration and longest-word algorithms do not by themselves yield the singleton-cut rigidity or missing intermediate lengths. This is a best-of-knowledge finding with a specific full-text access limitation, not a priority guarantee.

## value

PASS

For the natural one-letter rotation, the result explains why deletion-minimal (as opposed to shortest) words can jump from a unique shortest word to two much longer possible lengths, with an unbounded interval of absent lengths. The rigidity of the two shorter words and existence at the absolute 2n bound are independent structural information, not counts extrapolated from small alphabets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
