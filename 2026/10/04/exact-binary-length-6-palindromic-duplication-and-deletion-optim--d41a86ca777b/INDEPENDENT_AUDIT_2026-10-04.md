# Independent mathematical audit

## correctness

PASS

The channel definitions were reconstructed directly. An independent exact conflict-graph computation on all \(64\) length-six words gives \(56\) duplication-conflict edges and \(34\) deletion-conflict edges. Exact maximum-independent-set optimization returns \(40\) and \(42\), respectively. The package certificates independently realize the same bounds: a 40-word duplication packing plus 24 disjoint conflict edges, and a 42-word deletion packing plus a disjoint partition into eight conflict triangles, six conflict edges, and 28 singletons. These upper certificates are logically sufficient without relying on an optimizer.

## originality

PASS

The closest defining source uses exactly the binary \(n=6\), duplication length \(2\), one-error setting to demonstrate that palindromic duplication and deletion correction are not equivalent, but it does not determine either exact maximum code size. Later palindromic-duplication work inspected is asymptotic/general and does not supply the paired \(40\) versus \(42\) finite optimum. Targeted Resultary searches likewise found no covering exact result.

## value

PASS

The exact parameter is not arbitrary: it is the very binary length-six, block-length-two setting used in the foundational paper to demonstrate nonequivalence of palindromic duplication and deletion correction. Replacing witness-level nonequivalence by the exact extremal separation \(40<42\) gives a motivated quantitative answer and a reusable benchmark for this error model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
