# Independent mathematical audit

## correctness

PASS

The last letters of the complete greedy arches, followed by a letter absent from the remaining suffix, give a missing subsequence of length one beyond the arch count: each successive earliest match is the corresponding arch endpoint. For counting, the first complete arch has two choices at length two and two at length three. After any arch the terminal run has length one; there are two possible next arches of length two and one of length three, and the optional incomplete suffix has series 1+2t+t^2. With no complete arch the series is 1+2t+2t^2. Summing gives the displayed rational series. Each arch uses two or three bits and the suffix at most two; alternation and (001)^m followed by at most two zeros attain the endpoints, including the empty word case. At u=1 the simple positive dominant pole is separated from the other roots and its numerator is nonzero; analytic continuation gives a uniform exponential remainder locally. Differentiating its inverse-root equation in log u yields the stated first and positive second cumulant slopes, and the centered characteristic functions yield the normal law and rounded threshold. An independent direct count via run compositions and sets of position-subsequences agrees at n=0 through 14.

## originality

PASS

The arch characterization and general finite-length counting algorithms are prior work. The distinct claim supported for the frozen record is the joint all-length law with exact extremal and fluctuation behavior for uniform run-two words. No stronger earlier result was established that supplies that law. There are materially equivalent and broader indexed later statements; this judgment is not a claim that the formulas remain unique in the corpus or a conclusive priority ruling.

## value

PASS

For a natural regular constraint and a standard measure of scattered-subsequence coverage, the answer gives the exact law at every length, sharp attainable lengths, and a quantitative threshold for randomly sampled constrained words. In particular the small strictly positive variance constant is useful for distinguishing worst-case and typical coverage; it is not given by the generic finite-length algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
