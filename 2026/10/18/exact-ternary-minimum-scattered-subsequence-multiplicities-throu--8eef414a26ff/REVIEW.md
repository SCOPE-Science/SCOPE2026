# Independent mathematical audit

## correctness

PASS

The frozen recurrence partitions embeddings by use of the last text position. Nonzero base-four digits encode distinct patterns, appending multiplies the old code by four and adds a digit, the two streams are individually sorted, and the merge adds exactly the coinciding counts; the integer keys and counts cannot overflow through length 16. Restricted growth adds existing symbols or the next new one, giving one exemplar per relabeling class, including words omitting symbols and without reversal quotient. Independently enumerated all canonical words of each length 1..16 by base-three suffixes with leading 0 and discarding a 2 before the first 1. For each length, discarded only words with an explicit multiplicity above the tabulated target, calculated from a single-letter binomial or selected fixed-pattern integer DP. On all survivors, visited the trie of present patterns, using counts by final text position: the count for an extension ending at j sums all prefix counts ending before j. This checks every present pattern or finds a witness over the target. Thus all words at or below the target are recovered, and their exact scores certify the lower bound, not just attainability. The total at length 16 was 7,174,454 canonical texts, with 1,049 passing the preliminary sieve and exactly the four frozen optimizers at 46. The full lists, counts, minima and examples for all 16 lengths agree with data/census.json. Replay paths: /workspace/branches/independent_replays/replay5.py and replay5_1_13.jsonl, replay5_14_15.jsonl, replay5_16.jsonl in that directory. The submitted secondary checker alone exhausts only lengths through nine; the independent threshold census exhausts the whole claim. No inference beyond length 16.

## originality

PASS

The objective, recurrence idea and general-alphabet framework are already known, and trivial initial values are not a distinct contribution. The supported novel content is the nontrivial exact ternary finite profile with all relabeling-class optimizer sets through length 16, not a novelty claim about the minimax problem or the method. The strongest actual tables inspected are for a different alphabet.

## value

PASS

The minimum max-occurrence invariant is motivated by the existing subword entropy problem; complete first nonbinary data are useful for comparing proposed optimizer structure and alphabet-size bounds against exact outcomes. The substantial contiguous range and full optimizer lists, rather than an isolated small value, expose variation in structure: uniqueness at lengths 14 and 15, four relabeling classes at 16, and markedly larger sets at some smaller lengths. The certified lower bounds and equalities are useful independently of a future asymptotic theorem; neither the cutoff nor these data imply asymptotic behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
